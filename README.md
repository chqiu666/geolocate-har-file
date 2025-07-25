# 🌍 Web Network Distribution Analysis

This project analyzes different web network architectures by capturing and visualizing HAR (HTTP Archive) files, revealing the hidden geography of the web.

## 📋 Overview

HAR files contain detailed information about all network requests made by a web browser, including the IP addresses of servers that responded to each request. By geolocating these IP addresses, we can visualize how different types of web services distribute their infrastructure across the globe, revealing patterns of centralization, decentralization, and federation.

## 🎯 Key Findings

The geographic distribution of network requests reveals fundamental differences in web architecture:

- **🌐 Decentralized (YaCy)**: 10 unique global locations - truly distributed peer-to-peer network
- **🎥 Centralized (YouTube)**: 6 locations, all Google infrastructure - highly concentrated 
- **🐘 Federated (Mastodon)**: 9 independent instances - moderately distributed federation

## 📁 Project Structure

```
geolocate-har-file/
├── inputs/
│   ├── yacy-decentralized.har      # P2P search engine HAR
│   ├── youtube-centralized.har     # Centralized video platform HAR  
│   └── mastodon-federated.har      # Federated social network HAR
├── outputs/
│   ├── index.html                  # Main project showcase page
│   ├── network_comparison_map.html # Interactive comparison map
│   ├── yacy-decentralized_map.html # YaCy P2P network map
│   ├── youtube-centralized_map.html# YouTube centralized map
│   ├── mastodon-federated_map.html # Mastodon federation map
│   └── *.geojson                   # GeoJSON data files
├── scrape_har_locations.py         # Original HAR processing script
├── process_all_hars.py             # Batch processing script
└── create_comparison_map.py        # Comparison map generator
```

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mapping-systems/geolocate-har-file
   cd geolocate-har-file
   ```

2. **Install dependencies:**
   ```bash
   # On Ubuntu/Debian:
   sudo apt install python3-folium python3-requests python3-venv

   # Or using pip:
   pip install folium requests
   ```

3. **Run the analysis:**
   ```bash
   # Process individual HAR files:
   python3 scrape_har_locations.py

   # Process all HAR files:
   python3 process_all_hars.py

   # Create comparison map:
   python3 create_comparison_map.py
   ```

## 🗺️ Generated Maps

### 1. Interactive Comparison Map
**File:** `outputs/network_comparison_map.html`
- Toggle between different network types
- Compare geographic distribution patterns
- See all networks in one interactive view

### 2. Individual Network Maps
- **YaCy Decentralized:** `outputs/yacy-decentralized_map.html`
- **YouTube Centralized:** `outputs/youtube-centralized_map.html`  
- **Mastodon Federated:** `outputs/mastodon-federated_map.html`

### 3. Project Showcase
**File:** `outputs/index.html`
- Comprehensive overview of all maps
- Technical details and analysis
- Usage instructions

## 📊 Data Analysis

### Network Distribution Patterns

| Network Type | Unique IPs | Total Requests | Distribution Pattern |
|--------------|------------|----------------|---------------------|
| YaCy (P2P)   | 10         | 10            | Fully distributed   |
| YouTube      | 6          | 10            | Highly centralized  |
| Mastodon     | 9          | 10            | Moderately federated |

### Geographic Insights

- **Decentralized networks** show the most geographic diversity
- **Centralized networks** cluster around major data center hubs
- **Federated networks** balance independence with interconnection

## 🔍 How HAR File Analysis Works

1. **Capture:** Browser network activity is recorded in HAR format
2. **Extract:** IP addresses are extracted from server responses
3. **Geolocate:** IPs are resolved to geographic coordinates using ipinfo.io
4. **Visualize:** Locations are plotted on interactive maps using Folium
5. **Analyze:** Distribution patterns reveal network architecture

## 🌐 Network Types Explained

### Decentralized (P2P)
- **Example:** YaCy search engine
- **Pattern:** Each user runs their own node
- **Geography:** Truly global distribution
- **Resilience:** High - no single point of failure

### Centralized
- **Example:** YouTube/Google services
- **Pattern:** All requests flow through one company's infrastructure
- **Geography:** Concentrated in major data centers
- **Efficiency:** High - optimized for scale and performance

### Federated
- **Example:** Mastodon social network
- **Pattern:** Independent instances that can communicate
- **Geography:** Multiple centers of activity
- **Balance:** Moderate distribution with interconnection

## 🛠️ Technical Details

- **Data Source:** HAR files from browser network activity
- **Geolocation API:** ipinfo.io for IP-to-location mapping
- **Visualization:** Folium (Python wrapper for Leaflet.js)
- **Data Format:** GeoJSON for geographic data storage
- **Maps:** Interactive web maps with clustering and layer controls

## 📸 Usage Instructions

1. **Start with the comparison map** to see all networks at once
2. **Toggle layers** using controls in the top-right corner
3. **Click markers** for detailed server information
4. **Compare patterns** between centralized vs. decentralized networks
5. **Zoom and pan** to explore different world regions

## 🔬 Educational Value

This project demonstrates:
- How different web architectures distribute globally
- The geographic concentration of major tech platforms
- The potential for decentralized alternatives
- Methods for analyzing web infrastructure through HAR files
- Geographic patterns in internet infrastructure

## 🎓 Assignment Context

This project was completed as part of a web mapping course assignment focused on:
- Understanding HAR file structure and analysis
- Visualizing geographic patterns in web data
- Comparing different network architectures
- Creating interactive web maps for data exploration

## 📝 Submission

- ✅ Screenshot of the web map (comparison map)
- ✅ GeoJSON files for all network types
- ✅ Link to folder with web map files (can be launched locally)
- ✅ Analysis of different network distribution patterns

## 🚀 Future Enhancements

- Real-time HAR capture automation
- Additional network types (CDNs, blockchain networks)
- Performance metrics overlay
- Historical network evolution tracking
- API for programmatic access to maps

---

*This project reveals the hidden geography of the web, showing which parts of the internet are truly distributed and which remain concentrated in the hands of a few large companies.*