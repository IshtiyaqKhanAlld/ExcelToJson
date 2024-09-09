**Excel to JSON Converter** : 
This Python script provides a straightforward solution for converting Excel files to JSON format. It processes all Excel files in a specified folder, converting each one to a JSON file with the same name

**Features**
Batch Processing: Converts all .xlsx files in a specified directory.
Data Conversion: Reads Excel files into a pandas DataFrame and converts them to JSON format.
File Management: Saves the resulting JSON data to new files with the .json extension.

**Requirements**
Python 3.x
pandas library
openpyxl library (for reading Excel files)

**Installation**
Install Required Libraries: Make sure you have the necessary libraries installed. You can install them using pip:

bash
Copy code
pip install pandas openpyxl
Usage
Set Up Your Folder: Specify the path to the folder containing your Excel files by updating the folder_path variable in the script.

Run the Script: Execute the script in your Python environment. It will loop through each Excel file in the specified folder, convert it to JSON, and save the output in the same folder.

python
Copy code
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

    print(f"Converted {file} to {json_file_name
    
**Notes:**
Ensure the folder path is correctly specified and that it contains .xlsx files.
The script will save the JSON files in the same directory as the Excel files.
If working with large files, ensure you have sufficient memory and disk space available.

**Contributing:**
Feel free to fork the repository and contribute enhancements or bug fixes. For any issues or feature requests, please open an issue on GitHub.
