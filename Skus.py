import csv
import json
from collections import defaultdict

def csv_to_json_group_by_columns(csv_file_path, json_file_path, group_by_columns, array_columns, column_mapping):
    grouped_data = defaultdict(lambda: {"goods": [], "barcodes": set()})
    
    # Open the CSV file with UTF-8 encoding for handling Thai characters
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Group rows by the specified columns and collect other columns in arrays
        for row in csv_reader:
            # Rename the columns based on the mapping
            renamed_row = {column_mapping[key]: value for key, value in row.items() if key in column_mapping}
            
            group_key = tuple(renamed_row[col] for col in group_by_columns)  # Create a tuple from group-by columns
            array_data = {col: renamed_row[col] for col in array_columns}    # Collect remaining columns into a dictionary
            
            grouped_data[group_key]["goods"].append(array_data)
            grouped_data[group_key]["barcodes"].add(renamed_row['code'])     # Add 'code' to the 'barcodes' set
    
    # Convert the tuple keys back to dictionaries for JSON output
    output_data = []
    for key, values in grouped_data.items():
        group_dict = dict(zip(group_by_columns, key))
        group_dict['goods'] = values['goods']
        group_dict['barcodes'] = list(values['barcodes'])  # Convert set to list for JSON output
        output_data.append(group_dict)
    
    # Write the grouped data to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(output_data, json_file, indent=4, ensure_ascii=False)

# Example usage
column_mapping = {
    'SKU_NAME': 'name',
    'AP': 'ap',
    'IMG': 'img',
    'CAT': 'cat',
    'BRAND': 'bnd',
    'GOODS_CODE': 'code',
    'UTQ_NAME': 'utqName',
    'UTQ_QTY': 'utqQty',
    'PRICE_0': 'price0',
    'PRICE_8': 'price8'
}

group_by_columns = ['name', 'ap', 'img', 'cat', 'bnd']
array_columns = ['code', 'utqName', 'utqQty', 'price0', 'price8']

csv_to_json_group_by_columns('SKU.csv', 'SKUs.json', group_by_columns, array_columns, column_mapping)
