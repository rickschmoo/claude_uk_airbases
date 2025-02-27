import os
from dotenv import load_dotenv

import gmplot
import pandas as pd
import requests
from io import StringIO

# Function to get UK air base data
def get_uk_air_bases():
    # This is a simplified example - in a real application, you might:
    # 1. Use an API like OpenStreetMap or a military database
    # 2. Load from a local CSV file
    # For demonstration, I'll create a list of major UK air bases
    
    air_bases = [
        {"name": "RAF Brize Norton", "lat": 51.7504, "lon": -1.5836, "info": "Largest RAF station"},
        {"name": "RAF Coningsby", "lat": 53.0933, "lon": -0.1708, "info": "Home of Typhoon fighters"},
        {"name": "RAF Lossiemouth", "lat": 57.7052, "lon": -3.3397, "info": "Major fighter base in Scotland"},
        {"name": "RAF Northolt", "lat": 51.5530, "lon": -0.4166, "info": "London-area RAF station"},
        {"name": "RAF Lakenheath", "lat": 52.4090, "lon": 0.5610, "info": "USAF base in the UK"},
        {"name": "RAF Mildenhall", "lat": 52.3636, "lon": 0.4864, "info": "USAF operations base"},
        {"name": "RNAS Yeovilton", "lat": 51.0036, "lon": -2.6386, "info": "Royal Navy air station"},
        {"name": "RNAS Culdrose", "lat": 50.0860, "lon": -5.2573, "info": "Royal Navy helicopter base"},
        {"name": "RAF Valley", "lat": 53.2481, "lon": -4.5352, "info": "Training base in Wales"},
        {"name": "RAF Waddington", "lat": 53.1662, "lon": -0.5262, "info": "Intelligence and surveillance base"}
    ]
    
    return air_bases

# Load variables from .env file
load_dotenv()  

# Setup Google Maps API
AIRBASE_GOOGLE_API_KEY = os.environ.get('AIRBASE_GOOGLE_API_KEY', '')
print(AIRBASE_GOOGLE_API_KEY)

# Get UK air base data
uk_air_bases = get_uk_air_bases()

# Create map centered on UK
gmap = gmplot.GoogleMapPlotter(54.0, -2.0, 6, AIRBASE_GOOGLE_API_KEY)
# Replace "YOUR_GOOGLE_MAPS_API_KEY" with an actual API key from the Google Cloud Platform

# Add air bases to the map
for base in uk_air_bases:
    gmap.marker(
        base["lat"], 
        base["lon"], 
        title=base["name"],
        info_window=f"<h3>{base['name']}</h3><p>{base['info']}</p>"
    )

# You can customize with different marker colors or icons if needed
# Example with a different marker color:
# gmap.marker(lat, lng, color='blue')

# Save the map to an HTML file
gmap.draw("uk_air_bases_map.html")

print("Map created successfully! Open uk_air_bases_map.html in your browser.")
