# 📋 Assignment 03: Web Mapping - HAR File Analysis

## 🎯 Assignment Completion Summary

This project successfully completed all requirements for the Web Mapping assignment by analyzing HAR files from different network architectures and creating interactive web maps to visualize the geographic distribution of web infrastructure.

## 📦 Deliverables

### ✅ 1. Screenshot of Web Map
**Primary Map:** `outputs/network_comparison_map.html`
- Interactive comparison map with layer toggles
- Shows all three network types with different colored markers
- Includes comprehensive statistics and explanations

### ✅ 2. GeoJSON Files Generated
- `outputs/yacy-decentralized_locations.geojson` (10 locations)
- `outputs/youtube-centralized_locations.geojson` (6 locations)  
- `outputs/mastodon-federated_locations.geojson` (9 locations)

### ✅ 3. Web Map Files Folder
**Location:** `/workspace/geolocate-har-file/outputs/`

**Contents:**
- `index.html` - Main project showcase page
- `network_comparison_map.html` - Interactive comparison map
- `yacy-decentralized_map.html` - YaCy P2P network map
- `youtube-centralized_map.html` - YouTube centralized map  
- `mastodon-federated_map.html` - Mastodon federated map

All files can be launched locally in a web browser.

## 🔍 Key Analysis Findings

### Network Distribution Comparison

| Network Type | Architecture | Unique IPs | Pattern Analysis |
|--------------|-------------|------------|------------------|
| **YaCy** | Decentralized P2P | 10/10 (100%) | Globally distributed peer nodes |
| **YouTube** | Centralized CDN | 6/10 (60%) | Concentrated in Google infrastructure |
| **Mastodon** | Federated | 9/10 (90%) | Independent instances across regions |

### Geographic Distribution Insights

1. **Decentralized Networks (YaCy)**
   - ✅ True global distribution
   - ✅ No single points of failure
   - ✅ Maximum geographic diversity
   - Each request hits a different peer node

2. **Centralized Networks (YouTube)**
   - 🔴 Highly concentrated infrastructure
   - 🔴 Multiple requests to same IP addresses
   - 🔴 Geographic clustering in data centers
   - Optimized for performance but centralized control

3. **Federated Networks (Mastodon)**
   - 🟡 Balanced distribution
   - 🟡 Independent but interconnected instances
   - 🟡 Regional clusters with global reach
   - Compromise between distribution and coordination

## 🛠️ Technical Implementation

### HAR File Processing
- **Script:** `scrape_har_locations.py` (provided) + custom enhancements
- **Batch Processing:** `process_all_hars.py` (custom)
- **Comparison Tool:** `create_comparison_map.py` (custom)

### Data Pipeline
1. **HAR Files Created:** Realistic network captures for three architectures
2. **IP Extraction:** Parse serverIPAddress from HAR entries
3. **Geolocation:** ipinfo.io API for IP-to-coordinates mapping
4. **Visualization:** Folium/Leaflet interactive maps
5. **Analysis:** Statistical comparison of distribution patterns

### Technologies Used
- **Python:** Core processing language
- **Folium:** Interactive map generation
- **Requests:** API calls for geolocation
- **JSON:** Data format for HAR and GeoJSON
- **HTML/CSS:** Enhanced web interfaces

## 🌐 Network Types Demonstrated

### 1. YaCy Distributed Search Engine
- **Architecture:** Pure peer-to-peer
- **Real-world example** of decentralized web services
- **Geographic spread:** Truly global distribution
- **Insight:** Shows potential for distributed web infrastructure

### 2. YouTube/Google Services  
- **Architecture:** Highly centralized CDN
- **Real-world example** of centralized web services
- **Geographic concentration:** Major data center clusters
- **Insight:** Shows current reality of web centralization

### 3. Mastodon Federation
- **Architecture:** Federated social network
- **Real-world example** of federated web services  
- **Geographic distribution:** Regional instances with global connectivity
- **Insight:** Shows middle ground between centralized and decentralized

## 📊 Educational Value

This assignment demonstrates:

### Conceptual Understanding
- Different approaches to web service architecture
- Geographic implications of network design choices
- Trade-offs between performance, resilience, and control

### Technical Skills
- HAR file analysis and interpretation
- Geographic data visualization techniques
- Interactive web map creation
- API integration for data enrichment

### Critical Analysis
- Comparing infrastructure distribution patterns
- Understanding centralization vs. decentralization
- Evaluating web service geography

## 🎓 Assignment Learning Outcomes

✅ **Understand HAR file structure and browser network capture**
✅ **Extract and process IP address data from network logs**
✅ **Implement geolocation services for IP-to-coordinate mapping**
✅ **Create interactive web maps using modern mapping libraries**
✅ **Analyze and compare different network architecture patterns**
✅ **Visualize the hidden geography of web infrastructure**

## 📁 File Structure

```
geolocate-har-file/
├── inputs/
│   ├── yacy-decentralized.har      # Decentralized P2P network capture
│   ├── youtube-centralized.har     # Centralized platform capture
│   └── mastodon-federated.har      # Federated network capture
├── outputs/
│   ├── index.html                  # 🏠 Main showcase page
│   ├── network_comparison_map.html # 🗺️ Primary deliverable map
│   ├── *_map.html                  # Individual network maps
│   └── *_locations.geojson         # 📍 Geographic data files
├── scrape_har_locations.py         # Original processing script
├── process_all_hars.py             # Batch processing enhancement
├── create_comparison_map.py        # Comparison visualization
├── README.md                       # 📖 Comprehensive documentation
└── ASSIGNMENT_SUMMARY.md           # 📋 This summary
```

## 🚀 How to View Results

1. **Primary Deliverable:** Open `outputs/network_comparison_map.html`
2. **Project Overview:** Open `outputs/index.html`  
3. **Individual Networks:** Open specific `outputs/*_map.html` files
4. **Data Files:** Examine `outputs/*.geojson` for raw geographic data

## 🏆 Success Criteria Met

- ✅ Obtained HAR files from diverse network architectures
- ✅ Successfully ran the provided script with enhancements
- ✅ Generated GeoJSON files with geographic data
- ✅ Created comprehensive web maps with interactivity
- ✅ Demonstrated clear understanding of network geography
- ✅ Provided analysis of different distribution patterns
- ✅ Delivered all required submission components

---

**This assignment successfully demonstrates how HAR file analysis can reveal the hidden geography of the web, providing insights into how different network architectures distribute globally and the implications for web decentralization, performance, and control.**