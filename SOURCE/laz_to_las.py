import laspy

# paths (adjust as needed)
laz_file_path = r"Badlands.laz"
las_file_path = r"Badlands.las"

# read the .laz and immediately write out a .las
las = laspy.read(laz_file_path)
las.write(las_file_path)

print(f"Converted {laz_file_path} → {las_file_path}")
