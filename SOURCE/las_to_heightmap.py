import laspy
import numpy as np
from PIL import Image

las = laspy.read("Badlands.las")

# Extract X, Y, Z
xs = las.x
ys = las.y
zs = las.z

# Create grid
grid_size = 1024  # Set your desired resolution
x_min, x_max = xs.min(), xs.max()
y_min, y_max = ys.min(), ys.max()

x_bins = np.linspace(x_min, x_max, grid_size)
y_bins = np.linspace(y_min, y_max, grid_size)

# Create elevation grid
elevation = np.full((grid_size, grid_size), fill_value=np.nan)

for x, y, z in zip(xs, ys, zs):
    xi = np.searchsorted(x_bins, x) - 1
    yi = np.searchsorted(y_bins, y) - 1
    if 0 <= xi < grid_size and 0 <= yi < grid_size:
        if np.isnan(elevation[yi, xi]):
            elevation[yi, xi] = z
        else:
            elevation[yi, xi] = max(elevation[yi, xi], z)

# Normalize to 0-255
elevation = np.nan_to_num(elevation, nan=np.nanmin(elevation))
elevation -= elevation.min()
elevation /= elevation.max()
elevation *= 255

# Save as PNG
Image.fromarray(elevation.astype(np.uint8)).save("Badlands_Heightmap.png")
