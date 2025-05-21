import numpy as np
from PIL import Image

# Load the downsampled matrix from the CSV file
matrix = np.loadtxt('downsampled_matrix.csv', delimiter=',')

# Normalize the matrix to the 0-255 range
matrix_normalized = 255 * (matrix - matrix.min()) / (matrix.max() - matrix.min())
matrix_normalized = matrix_normalized.astype(np.uint8)

# Create an image from the normalized matrix
image = Image.fromarray(matrix_normalized, mode='L')

# Save the image
image.save('downsampled_matrix_grayscale.bmp')

print("Grayscale bitmap image has been saved as 'downsampled_matrix_grayscale.bmp'")
