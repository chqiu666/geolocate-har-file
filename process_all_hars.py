import json
import requests
import folium
from folium.plugins import MarkerCluster
from pathlib import Path
from typing import List, Tuple
import os

# Configuration
HAR_FILES = {
    "yacy-decentralized": "inputs/yacy-decentralized.har",
    "youtube-centralized": "inputs/youtube-centralized.har", 
    "mastodon-federated": "inputs/mastodon-federated.har"
}
MAX_IPS = 50

def load_ips_from_har(path: str) -> List[Tuple[str, str]]:
    """Extract unique IP addresses from a HAR file."""
    with open(path, "r", encoding="utf-8") as f:
        har = json.load(f)

    entries = har.get("log", {}).get("entries", [])
    ips = set()
    for entry in entries:
        ip = entry.get("serverIPAddress")
        url = entry.get("request", {}).get("url", "")
        print(f"Processing entry: {url} with IP: {ip}")
        if ip:
            ip = ip.strip("[]")
            ips.add((ip, url))
    return list(ips)

def geolocate_ip(ip_item: Tuple[str, str]) -> Tuple[str, float, float, str]:
    """Geolocate IP using ipinfo.io API. Returns (ip, lat, lon, url)."""
    ip, url = ip_item

    try:
        resp = requests.get(f"https://ipinfo.io/{ip}/json")
        data = resp.json()
        loc = data.get("loc")
        if loc:
            lat, lon = map(float, loc.split(","))
            return ip, lat, lon, url
    except Exception as e:
        print(f"Error locating {ip}: {e}")
    return ip, 0, 0, url

def build_map(ip_locations: List[Tuple[str, float, float, str]], output_path: str, geojson_path: str) -> None:
    """Generate Folium map from list of IP + lat/lon tuples."""
    m = folium.Map(location=[20, 0], zoom_start=2)
    cluster = MarkerCluster().add_to(m)
    
    for ip, lat, lon, url in ip_locations:
        if lat and lon:
            folium.Marker(
                location=[lat, lon],
                popup=f"IP: {ip}<br>URL: {url}",
                icon=folium.Icon(color="blue", icon="info-sign"),
            ).add_to(cluster)

    # Save data as a GeoJSON file
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"ip": ip, "url": url},
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat],
                },
            }
            for ip, lat, lon, url in ip_locations
            if lat and lon
        ],
    }

    m.save(output_path)
    print(f"Map saved to: {output_path}")

    with open(geojson_path, "w", encoding="utf-8") as f:
        json.dump(geojson_data, f)
    print(f"GeoJSON saved to: {geojson_path}")

def process_har_file(name: str, har_file: str):
    """Process a single HAR file."""
    print(f"\n=== Processing {name} ===")
    
    ip_list = load_ips_from_har(har_file)
    print(f"Found {len(ip_list)} IPs")

    # Deduplicate by IP only
    ips_dict = {}
    for ip, url in ip_list:
        if ip not in ips_dict:
            ips_dict[ip] = url
    ips = list(ips_dict.items())
    print(f"Unique IPs: {len(ips)}")
    
    ip_locations = [geolocate_ip(ip) for ip in ips[:MAX_IPS]]
    
    output_map = f"outputs/{name}_map.html"
    output_geojson = f"outputs/{name}_locations.geojson"
    
    build_map(ip_locations, output_map, output_geojson)

if __name__ == "__main__":
    # Create outputs directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)
    
    # Process each HAR file
    for name, har_file in HAR_FILES.items():
        if os.path.exists(har_file):
            process_har_file(name, har_file)
        else:
            print(f"HAR file not found: {har_file}")