import pandas as pd
import requests
import io

# API URL
api_url = 'https://analisi.transparenciacatalunya.cat/resource/gn9e-3qhr.csv'

# Fetch data from the API
response = requests.get(api_url)
data = response.text

# Read the CSV data into a DataFrame
df = pd.read_csv(io.StringIO(data))


# Print columns
print(df.columns)

# Separate 'estaci' into 'Name' and 'Poble'
df[['Name', 'Poble']] = df['estaci'].str.split('(', expand=True)

# Remove trailing whitespace from 'Poble' column
df['Poble'] = df['Poble'].str.rstrip(')')

# Set 'Poble' to 'Riudecanyes' for 'Embassament de Riudecanyes'
df.loc[df['Name'] == 'Embassament de Riudecanyes', 'Poble'] = 'Riudecanyes'

# Convert 'dia' to datetime and create 'Mes' and 'Any' columns
df['dia'] = pd.to_datetime(df['dia'])
df['Mes'] = df['dia'].dt.month
df['Any'] = df['dia'].dt.year

# Reorder the columns
df = df[['dia', 'Name', 'Poble', 'Mes', 'Any', 'nivell_absolut', 'percentatge_volum_embassat', 'volum_embassat']]

# Rename headers
df = df.rename(columns={
    'dia': 'Dia',
    'nivell_absolut': 'Nivell absolut',
    'percentatge_volum_embassat': 'Percentatge volum embassat',
    'volum_embassat': 'Volum embassat'
})

# Remove leading and trailing whitespaces from 'Name' column
df['Name'] = df['Name'].str.strip()

# Create a mapping of towns to regions
comarca_mapping = {
    'Navès': 'Solsonés',
    'Darnius': 'Alt Empordà',
    'Castellet i la Gornal': 'Alt Penedès',
    'Clariana de Cardener': 'Solsonés',
    'Osor': 'Selva',
    'Cercs': 'Berguedà',
    'Cornudella de Montsant': 'Priorat',
    'Vilanova de Sau': 'Osona',
    'Riudecanyes': 'Baix Camp'
}

# Create 'Comarca' column based on the mapping
df['Comarca'] = df['Poble'].map(comarca_mapping)

# Print the cleaned dataframe
print(df)

# Save the cleaned dataframe to a new CSV file
df.to_csv('cleaned_pantans_api.csv', index=False)