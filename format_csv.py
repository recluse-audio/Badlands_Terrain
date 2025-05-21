import csv

input_file = 'downsampled_matrix.csv'  # replace with your CSV file path
output_file = 'badlands_coll.txt'

with open(input_file, 'r') as csvfile, open(output_file, 'w') as txtfile:
    csvreader = csv.reader(csvfile)
    row_num = 0
    for row in csvreader:
        formatted_row = f'{row_num}, {", ".join(row)};'
        txtfile.write(formatted_row + '\n')
        row_num += 1
