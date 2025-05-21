import pandas as pd
import laspy
import numpy as np

# Specify the .laz file path
laz_file_path = 'Badlands.laz'
csv_file_path = 'Badlands_raw.csv'

# Read the .laz file with laspy
with laspy.open(laz_file_path) as laz_file:
    las_data = laz_file.read()

# Extract point data
point_records = las_data.points

# Create a DataFrame from the point records
df = pd.DataFrame({
    'X': point_records.X,
    'Y': point_records.Y,
    'Z': point_records.Z
    # 'intensity': point_records.intensity,
    # 'return_number': point_records.return_number,
    # 'number_of_returns': point_records.number_of_returns,
    # 'scan_direction_flag': point_records.scan_direction_flag,
    # 'edge_of_flight_line': point_records.edge_of_flight_line,
    # 'classification': point_records.classification,
    # 'scan_angle_rank': point_records.scan_angle_rank,
    # 'user_data': point_records.user_data,
    # 'point_source_id': point_records.point_source_id,
    # 'gps_time': point_records.gps_time
})

# Normalize the X and Y values
df['X'] = df['X'] - df['X'].min()
df['Y'] = df['Y'] - df['Y'].min()
df['Z'] = df['Z'] - df['Z'].min()

# Normalize to 0-1 range
df['X'] = df['X'] / df['X'].max()
df['Y'] = df['Y'] / df['Y'].max()
df['Z'] = df['Z'] / df['Z'].max()

# Scale to target dimensions
target_width = 1440
target_height = 1080
df['X'] = (df['X'] * (target_width - 1)).astype(int)
df['Y'] = (df['Y'] * (target_height - 1)).astype(int)

# Ensure indices are within range
df = df[(df['X'] >= 0) & (df['X'] < target_width) & (df['Y'] >= 0) & (df['Y'] < target_height)]

# Create an empty matrix
matrix = np.zeros((target_height, target_width))

# Handle duplicate indices by averaging Z values
df_grouped = df.groupby(['X', 'Y']).mean().reset_index()

# Fill the matrix with Z values
for index, row in df.iterrows():
    matrix[row['Y'], row['X']] = row['Z']

# Downsampling by taking the mean of the values in each bin (optional)
downsampled_matrix = matrix.reshape(target_height, -1, target_width, -1).mean(axis=(1, 3))

print(downsampled_matrix)

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Conversion complete. CSV file saved to {csv_file_path}")
