import pandas as pd
import requests
import io

# Read the CSV file
# src: https://analisi.transparenciacatalunya.cat/Medi-Ambient/Quantitat-d-aigua-als-embassaments-de-les-Conques-/gn9e-3qhr
df = pd.read_csv('Quantitat_d_aigua_als_embassaments_de_les_Conques_Internes_de_Catalunya.csv')

# Separate 'Estació' into 'Name' and 'Poble'
df[['Name', 'Poble']] = df['Estació'].str.split('(', expand=True)

# Remove trailing whitespace from 'Poble' column
df['Poble'] = df['Poble'].str.rstrip(')')

# Set 'Poble' to 'Riudecanyes' for 'Embassament de Riudecanyes'
df.loc[df['Name'] == 'Embassament de Riudecanyes', 'Poble'] = 'Riudecanyes'

# Convert 'Dia' to datetime and create 'Mes' and 'Any' columns
df['Dia'] = pd.to_datetime(df['Dia'], format='%d/%m/%Y')
df['Mes'] = df['Dia'].dt.month
df['Any'] = df['Dia'].dt.year

# Drop the original 'Estació' column
df = df.drop(columns=['Estació'])

# Reorder the columns
df = df[['Dia', 'Name', 'Poble', 'Mes', 'Any', 'Nivell absolut (msnm)', 'Percentatge volum embassat (%)', 'Volum embassat (hm3)']]

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
df.to_csv('cleaned_pantans_dataset.csv', index=False)