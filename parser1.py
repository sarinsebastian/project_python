import random
import string
import csv

# Define column names and offsets
column_names = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"]
offsets = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]
fixed_width_encoding = "windows-1252"
include_header = True
delimited_encoding = "utf-8"

# Function to generate realistic sample data
def generate_sample_data():
    def random_string(length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    # Generate data for each column with specified width
    return [
        random_string(width).ljust(width)[:width] for width in offsets
    ]

# Create a tab-delimited data file
def create_tab_delimited_file(filename, num_records=10):
    with open(filename, 'w') as file:
        for _ in range(num_records):
            record = generate_sample_data()
            # Join fields with a tab character
            line = '\t'.join(record)
            file.write(line + '\n')

# Create a tab-delimited data file named 'tab_delimited_data.txt'
create_tab_delimited_file('tab_delimited_data.txt', num_records=10)

# Function to parse the fixed-width file and convert to CSV
def fixed_width_to_csv(fixed_width_file, csv_file):
    # Open the input and output files
    with open(fixed_width_file, 'r', encoding=fixed_width_encoding) as infile, \
         open(csv_file, 'w', newline='', encoding=delimited_encoding) as outfile:
        
        # Initialize the CSV writer
        writer = csv.writer(outfile)
        
        # Write the header if required
        if include_header:
            writer.writerow(column_names)
        
        # Iterate through each line of the fixed-width file
        for line in infile:
            # Initialize the starting index
            start_index = 0
            row = []
            
            # Extract each field based on the given offsets
            for offset in offsets:
                print(offset)
                # Extract the field value based on the offset length and strip extra spaces
                field_value = line[start_index:start_index + offset].strip()
                print(field_value)
                row.append(field_value)
                # Update the start index to the next field's position
                start_index += offset
            
            # Write the row to the CSV
            writer.writerow(row)

# Example usage
fixed_width_to_csv(r'tab_delimited_data.txt', 'output.csv')
