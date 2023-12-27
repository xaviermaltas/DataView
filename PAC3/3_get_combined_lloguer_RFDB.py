# import pandas as pd

# # Load data from the first CSV file
# rent_data = pd.read_csv('1_lloguer_comarques.csv')

# # Load data from the second CSV file
# income_data = pd.read_csv('2_RFDB_habitant_comarques.csv')

# # Merge the two dataframes based on 'Comarca' and 'Any' columns
# merged_data = pd.merge(rent_data, income_data, on=['Comarca', 'Any'], suffixes=('_rent', '_income'))

# # Save the merged data to a new CSV file
# merged_data.to_csv('3_combined_lloguerRFDB.csv', index=False)

# print("Combined data saved to combined_data.csv")




import pandas as pd

# Load data from the first CSV file
rent_data = pd.read_csv('1_lloguer_comarques.csv')

# Load data from the second CSV file
income_data = pd.read_csv('2_RFDB_habitant_comarques.csv')

# Merge the two dataframes based on 'Comarca' and 'Any' columns
merged_data = pd.merge(rent_data, income_data, on=['Comarca', 'Any'], suffixes=('_rent', '_income'))

# Convert 'RFDB per habitant (milers d'euros)' to thousands
merged_data['RFDB per habitant (milers d\'euros)'] *= 1000

# Add a new column 'RFDB per habitant - Mensual' by dividing the transformed column by 12
merged_data['RFDB per habitant - Mensual'] = merged_data['RFDB per habitant (milers d\'euros)'] / 12

# Truncate the decimals on the 'RFDB per habitant - Mensual' column to 2 decimals
merged_data['RFDB per habitant - Mensual'] = merged_data['RFDB per habitant - Mensual'].round(2)

# Sort the dataframe by the 'Any' (year) column in ascending order
merged_data = merged_data.sort_values(by='Any')

# Save the merged data to a new CSV file
merged_data.to_csv('3_combined_lloguerRFDB.csv', index=False)

print("Combined data with new column saved to combined_data.csv")
