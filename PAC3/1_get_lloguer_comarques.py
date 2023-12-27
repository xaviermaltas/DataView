import pandas as pd

def adjust_years(df):
    min_year = df['Any'].min()
    df['Any'] = 2022 - (df['Any'] - min_year)
    
    # Set count 9 and 10 to the year 2014
    df.loc[df['Any'].isin([9, 10]), 'Any'] = 2014
    
    # Keep count 11 as it is (no change)
    
    return df

def convert_excel_to_csv(excel_file_path, csv_output_path, sheet_name='Lloguer_anual'):
    # Specify the engine as 'openpyxl' to handle xlsx files
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=None, engine='openpyxl')

    # Find the row index where 'Comarques' is present in the first column
    comarques_row_index = df[df[0] == 'Comarques'].index[0]

    # Skip rows till the 'Comarques' row
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name, skiprows=comarques_row_index, header=None, engine='openpyxl')

    # Find the index of 'Vallès Oriental' and select the relevant rows
    valles_oriental_index = df[df[0] == 'Vallès Oriental'].index[0]
    df = df.iloc[:valles_oriental_index + 1, :]

    # Melt the DataFrame to convert it to a long format
    df_melted = pd.melt(df, id_vars=df.columns[0], var_name='Any')

    # Drop rows where 'value' is NaN
    df_melted = df_melted.dropna(subset=['value'])

    # Rename columns
    df_melted.columns = ['Comarca', 'Any', 'Preu mitjà lloguer']

    # Exclude rows where the year is 10
    df_melted = df_melted[df_melted['Any'] != 10]

    # Increase years from 11 to 19 by 1
    df_melted.loc[df_melted['Any'].isin(range(11, 20)), 'Any'] -= 1

    # Adjust the years using the custom function
    df_melted = adjust_years(df_melted)

    # Save the result to a CSV file
    df_melted.to_csv(csv_output_path, index=False)

if __name__ == "__main__":
    excel_file_path = 'ambits_anual_lloguer.xlsx'
    csv_output_path = '1_lloguer_comarques.csv'
    sheet_name = 'Lloguer_anual'

    convert_excel_to_csv(excel_file_path, csv_output_path, sheet_name)
