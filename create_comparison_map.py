import json
import folium
from folium.plugins import MarkerCluster
import os

def load_geojson(file_path):
    """Load GeoJSON data from file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def create_comparison_map():
    """Create a comprehensive comparison map with layer toggles."""
    
    # Load the GeoJSON data
    yacy_data = load_geojson('outputs/yacy-decentralized_locations.geojson')
    youtube_data = load_geojson('outputs/youtube-centralized_locations.geojson')
    mastodon_data = load_geojson('outputs/mastodon-federated_locations.geojson')
    
    # Create base map
    m = folium.Map(
        location=[20, 0], 
        zoom_start=2,
        tiles=None
    )
    
    # Add different base tiles
    folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)
    folium.TileLayer('cartodbpositron', name='CartoDB Positron').add_to(m)
    folium.TileLayer('cartodbdark_matter', name='CartoDB Dark').add_to(m)
    
    # Create feature groups for each network type
    yacy_group = folium.FeatureGroup(name='🌐 YaCy (Decentralized P2P)', show=True)
    youtube_group = folium.FeatureGroup(name='🎥 YouTube (Centralized)', show=False)
    mastodon_group = folium.FeatureGroup(name='🐘 Mastodon (Federated)', show=False)
    
    # Add YaCy markers (Green - Decentralized)
    for feature in yacy_data['features']:
        coords = feature['geometry']['coordinates']
        props = feature['properties']
        folium.Marker(
            location=[coords[1], coords[0]],
            popup=f"<b>Decentralized P2P</b><br>IP: {props['ip']}<br>URL: {props['url']}",
            icon=folium.Icon(color='green', icon='share-alt', prefix='fa'),
            tooltip="YaCy P2P Node"
        ).add_to(yacy_group)
    
    # Add YouTube markers (Red - Centralized)  
    for feature in youtube_data['features']:
        coords = feature['geometry']['coordinates']
        props = feature['properties']
        folium.Marker(
            location=[coords[1], coords[0]],
            popup=f"<b>Centralized CDN</b><br>IP: {props['ip']}<br>URL: {props['url']}",
            icon=folium.Icon(color='red', icon='play', prefix='fa'),
            tooltip="Google/YouTube Server"
        ).add_to(youtube_group)
    
    # Add Mastodon markers (Blue - Federated)
    for feature in mastodon_data['features']:
        coords = feature['geometry']['coordinates']
        props = feature['properties']
        folium.Marker(
            location=[coords[1], coords[0]],
            popup=f"<b>Federated Instance</b><br>IP: {props['ip']}<br>URL: {props['url']}",
            icon=folium.Icon(color='blue', icon='users', prefix='fa'),
            tooltip="Mastodon Instance"
        ).add_to(mastodon_group)
    
    # Add feature groups to map
    yacy_group.add_to(m)
    youtube_group.add_to(m)
    mastodon_group.add_to(m)
    
    # Add layer control
    folium.LayerControl(position='topright', collapsed=False).add_to(m)
    
    # Add custom HTML with statistics and explanation
    stats_html = f"""
    <div style="position: fixed; 
                top: 10px; left: 10px; width: 350px; height: auto; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:14px; padding: 10px">
    <h3>🌍 Web Network Distribution Analysis</h3>
    <p><strong>This map visualizes different network architectures by analyzing HAR files:</strong></p>
    
    <h4>📊 Statistics:</h4>
    <ul>
        <li><span style="color:green;">🌐 YaCy (Decentralized):</span> {len(yacy_data['features'])} unique server locations</li>
        <li><span style="color:red;">🎥 YouTube (Centralized):</span> {len(youtube_data['features'])} unique server locations</li>
        <li><span style="color:blue;">🐘 Mastodon (Federated):</span> {len(mastodon_data['features'])} unique server locations</li>
    </ul>
    
    <h4>🔍 Network Types:</h4>
    <ul>
        <li><strong>Decentralized:</strong> Truly distributed peer-to-peer network</li>
        <li><strong>Centralized:</strong> All requests go to one company's infrastructure</li>
        <li><strong>Federated:</strong> Independent instances that can communicate</li>
    </ul>
    
    <p><small>💡 Use the layer controls to toggle between different network types and observe the geographic distribution patterns.</small></p>
    </div>
    """
    m.get_root().html.add_child(folium.Element(stats_html))
    
    # Save the map
    output_file = 'outputs/network_comparison_map.html'
    m.save(output_file)
    print(f"Comparison map saved to: {output_file}")
    
    return output_file

if __name__ == "__main__":
    create_comparison_map()