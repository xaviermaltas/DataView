import pandas as pd

def get_min_and_target_year_values(dataframe, target_year):
    # Get the rows for the minimum year for each country
    min_year_values = dataframe.loc[dataframe.groupby('Country')['Year'].idxmin()]

    # Get the rows for the target year for each country
    target_year_values = dataframe[dataframe['Year'] == target_year]

    # Concatenate the two dataframes to get two rows per country
    result = pd.concat([min_year_values, target_year_values])

    # Sort the result by 'Country'
    result.sort_values('Country', inplace=True)

    return result

# Read the input CSV file with headers
#Data source -> https://www.kaggle.com/datasets/luxoloshilofunde/life-expectancy-vs-gdp-19502018
input_file = 'Life Expectancy vs GDP 1950-2018.csv'
df = pd.read_csv(input_file)

# Set the target year
target_year = 2018

# Get values for the minimum year and the target year
result_df = get_min_and_target_year_values(df, target_year)

# Save the result to a new CSV file
output_file = 'output_data.csv'
result_df.to_csv(output_file, index=False)

print(f"Output saved to {output_file}")
