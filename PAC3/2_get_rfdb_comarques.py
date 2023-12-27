# import csv

# def extract_rows(input_file, output_file, year):
#     # Flag to indicate when to start and stop extracting rows
#     extracting = False

#     # Create a new CSV file with the extracted rows
#     with open(input_file, 'r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         header = next(reader)

#         # Modify the header
#         new_header = ['Comarca', 'RFDB (milers d\'euros)', 'RFDB per habitant (milers d\'euros)', 'Índex Catalunya=100 per habitant', 'Year']

#         # Create a new CSV file with the modified header
#         with open(output_file, 'w', newline='', encoding='utf-8') as output:
#             writer = csv.writer(output)
#             writer.writerow(new_header)

#             for row in reader:
#                 if row and row[0] == 'Alt Camp':
#                     extracting = True
#                 if extracting:
#                     row.append(year)
#                     writer.writerow(row)
#                 if row and row[0] == 'Vallès Oriental':
#                     extracting = False
#                     break

#     print(f"New CSV file '{output_file}' created with the extracted rows and 'Year' column.")

# # Example usage:
# input_file = 'renda_files/2008.csv'  # Replace with your actual file path
# output_file = 'output_file_extracted.csv'  # Replace with your desired output file path
# year = 2008  # Replace with the actual year
# extract_rows(input_file, output_file, year)




import csv
import os

def extract_rows(input_directory, output_file):
    # Modify the header
    new_header = ['Comarca', 'RFDB (milers d\'euros)', 'RFDB per habitant (milers d\'euros)', 'Índex Catalunya=100 per habitant', 'Any']

    # Create a new CSV file with the modified header
    with open(output_file, 'w', newline='', encoding='utf-8') as output:
        writer = csv.writer(output)
        writer.writerow(new_header)

        # Iterate through all CSV files in the input directory
        for filename in os.listdir(input_directory):
            if filename.endswith(".csv"):
                year = int(os.path.splitext(filename)[0])  # Extract the year from the filename
                file_path = os.path.join(input_directory, filename)

                # Flag to indicate when to start and stop extracting rows
                extracting = False

                # Read the data from the current CSV file and append it to the output file
                with open(file_path, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    header = next(reader)  # Skip the header

                    for row in reader:
                        if row and row[0] == 'Alt Camp':
                            extracting = True
                        if extracting:
                            row.append(year)
                            writer.writerow(row)
                        if row and row[0] == 'Vallès Oriental':
                            extracting = False
                            break

    print(f"New CSV file '{output_file}' created with the extracted rows and 'Any' column.")

# Example usage:
input_directory = 'renda_files'  # Replace with your actual directory path
output_file = '2_RFDB_habitant_comarques.csv'  # Replace with your desired output file path
extract_rows(input_directory, output_file)