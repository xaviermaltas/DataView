from flask import Flask, render_template
import folium
import pandas as pd
import json

app = Flask(__name__)

# Read swamp data from CSV file with name and coordinates (Latitude, Longitude)
swamps_df = pd.read_csv("swamps_data.csv")

# Read additional data from cleaned_pantans_dataset.csv
additional_data_df = pd.read_csv("cleaned_pantans_dataset.csv")

# Merge the two dataframes on the 'Name' column
combined_df = pd.merge(swamps_df, additional_data_df, on='Name')

class SwampRecord:
    def __init__(self, day, month, year, nivell_absolut, percentatge_volum_embassat, volum_embassat):
        self.day = day
        self.month = month
        self.year = year
        self.nivell_absolut = nivell_absolut
        self.percentatge_volum_embassat = percentatge_volum_embassat
        self.volum_embassat = volum_embassat

class Swamp:
    def __init__(self, name, poble, comarca, max_capacity, coordinates):
        self.name = name
        self.poble = poble
        self.comarca = comarca
        self.coordinates = coordinates
        self.max_capacity = max_capacity
        self.records = []

# Create a dictionary to hold Swamp objects with the swamp name as the key
swamps_data_dict = {}

# Populate the dictionary with Swamp objects
for _, row in combined_df.iterrows():
    swamp_name = row['Name']

    # Create a Swamp object if it doesn't exist in the dictionary
    if swamp_name not in swamps_data_dict:
        coordinates = {'Latitude': row['Latitude'], 'Longitude': row['Longitude']}
        swamps_data_dict[swamp_name] = Swamp(swamp_name, row['Poble'], row['Comarca'], row['MaxVolume (hm3)'], coordinates)

    # Create a SwampRecord object for each row and append to the records list
    record = SwampRecord(row['Dia'], row['Mes'], row['Any'], row['Nivell absolut (msnm)'],
                         row['Percentatge volum embassat (%)'], row['Volum embassat (hm3)'])
    swamps_data_dict[swamp_name].records.append(record)

# Convert the dictionary values to a list of Swamp objects
swamps_data = list(swamps_data_dict.values())

# Print information for each swamp and the number of registers
# for swamp in swamps_data:
#     print(f"\nSwamp: {swamp.name}")
#     print(f"Poble: {swamp.poble}")
#     print(f"Comarca: {swamp.comarca}")
#     print(f"Coordinates: {swamp.coordinates}")
#     print(f"Number of Registers: {len(swamp.records)}")


# Convert Swamp objects to dictionaries
swamps_data_dict_for_template = [{ 
    'name': swamp.name, 
    'poble': swamp.poble, 
    'comarca': swamp.comarca, 
    'coordinates': swamp.coordinates, 
    'max_capacity': swamp.max_capacity,
    'records': [{'day': record.day, 'month': record.month, 'year': record.year,
                 'nivell_absolut': record.nivell_absolut, 
                 'percentatge_volum_embassat': record.percentatge_volum_embassat, 
                 'volum_embassat': record.volum_embassat}
                for record in swamp.records]
    } 
    for swamp in swamps_data]

@app.route('/')
def index():
    return render_template("index.html", swamps_data=swamps_data_dict_for_template)

if __name__ == '__main__':
    app.run(debug=True)
