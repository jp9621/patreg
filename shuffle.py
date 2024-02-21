import csv
import random

def shuffle_csv(input_file, output_file):
    # Read the CSV file into a list of rows
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # Shuffle the rows
    random.shuffle(rows)

    # Write the shuffled rows to a new CSV file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

# Example usage
input_file = 'st/st_data.csv'  # Replace 'input.csv' with the path to your input CSV file
output_file = 'st/st_data_shuff.csv'  # Replace 'shuffled_output.csv' with the desired output file path
shuffle_csv(input_file, output_file)
