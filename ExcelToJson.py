import os
import pandas as pd

# Specify the folder path containing Excel files
folder_path = 'path_to_your_folder'

# Get a list of all Excel files in the folder
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Loop through each Excel file and convert it to JSON
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)

    # Convert the DataFrame to JSON
    json_data = df.to_json(orient='records', indent=4)

    # Save the JSON data to a file
    json_file_name = file.replace('.xlsx', '.json')
    json_file_path = os.path.join(folder_path, json_file_name)
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

    print(f"Converted {file} to {json_file_name}")
