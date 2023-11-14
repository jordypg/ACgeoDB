import pandas as pd

def extract_values(input_file):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)

    # Create an empty list to store objects
    objects_list = []

    # Iterate through each row in the DataFrame
    for index in range(1, len(df)):
        row = df.iloc[index]
        # Extract values from columns 3 to 109
        values = row.iloc[2:109].tolist()

        # Create an object (you can use a dictionary or a custom class)
        obj = {'row_number': index + 1, 'values': values}

        # Append the object to the list
        objects_list.append(obj)

    return objects_list

if __name__ == "__main__":
    # Use the relative path for the Excel file
    excel_file_path = 'Study Away Eval S23 AY2223 for CS class.xlsx'

    # Call the function and get the list of objects
    extracted_objects = extract_values(excel_file_path)

    # Print the extracted objects
    for obj in extracted_objects:
        print(f"Row {obj['row_number']}: {obj['values']}")
    
    #first_object = extracted_objects[0] if extracted_objects else None
    #print(first_object['values'])
