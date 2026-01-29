import numpy as np

# Load the downsampled matrix from the CSV file
matrix = np.loadtxt('downsampled_matrix.csv', delimiter=',')

# Define the target dimensions
target_width = 1440
target_height = 1080

# Open a new text file to write the formatted data
with open('formatted_matrix.txt', 'w') as file:
    # Loop through each element in the matrix
    for y in range(target_height):
        for x in range(target_width):
            # Get the Z value at the current (x, y) index
            z = matrix[y, x]
            # Write the (x, y, z) values to the text file
            file.write(f'{x}, {y}, {z},\n')

print("Formatted data has been written to 'formatted_matrix.txt'")
