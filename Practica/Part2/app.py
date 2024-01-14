from flask import Flask, render_template
import folium
import pandas as pd

app = Flask(__name__)

# Read swamp data from CSV file with name and coordinates (Latitude, Longitude)
swamps_df = pd.read_csv("swamps_data.csv")

@app.route('/')
def index():
    # Create a map centered around Catalunya, Spain
    m = folium.Map(location=[41.8781, 1.85], zoom_start=9, tiles='OpenStreetMap')

    # Add markers for each swamp from the CSV file
    for _, swamp in swamps_df.iterrows():
        folium.Marker(
            [swamp["Latitude"], swamp["Longitude"]], 
            popup=swamp["Name"]
        ).add_to(m)

    # Save the map to an HTML file
    map_file_path = "templates/map.html"
    m.save(map_file_path)

    # Render the HTML file
    return render_template("map.html", map_file_path=map_file_path)

if __name__ == '__main__':
    app.run(debug=True)