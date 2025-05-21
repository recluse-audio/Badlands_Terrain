import laspy
import numpy as np
import matplotlib.pyplot as plt

# Path to the LAZ file
laz_file_path = 'Badlands.laz'

# Read the .laz file with laspy
with laspy.open(laz_file_path) as laz_file:
    las_data = laz_file.read()

# Extract point data
x = las_data.x
y = las_data.y
z = las_data.z

# Normalize the coordinates to 0-1 range
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())
z = (z - z.min()) / (z.max() - z.min())

# Scale to target dimensions
target_width = 1440
target_height = 1080
x = (x * (target_width - 1)).astype(int)
y = (y * (target_height - 1)).astype(int)

# Create an empty matrix for Z values
matrix = np.zeros((target_height, target_width))

# Fill the matrix with Z values, averaging duplicates
for i in range(len(x)):
    matrix[y[i], x[i]] += z[i]

# Handle duplicates by dividing by the count
counts = np.zeros((target_height, target_width))
for i in range(len(x)):
    counts[y[i], x[i]] += 1

# Avoid division by zero
counts[counts == 0] = 1
matrix /= counts

# Save the matrix to a CSV file
np.savetxt('downsampled_matrix.csv', matrix, delimiter=',')

# Load the matrix from the CSV file (for testing purposes)
loaded_matrix = np.loadtxt('downsampled_matrix.csv', delimiter=',')

# Create a meshgrid for plotting
xx, yy = np.meshgrid(np.arange(target_width), np.arange(target_height))

# Flatten the arrays for scatter plot
xx_flat = xx.flatten()
yy_flat = yy.flatten()
matrix_flat = loaded_matrix.flatten()

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xx_flat, yy_flat, matrix_flat, c=matrix_flat, cmap='viridis', marker='.', s=1)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
