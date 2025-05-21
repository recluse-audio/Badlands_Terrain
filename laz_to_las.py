import laspy

laz_file_path = '/Users/ryandevens/PROJECTS/BADLANDS/Badlands.laz'
las_file_path = '/Users/ryandevens/PROJECTS/BADLANDS/Badlands.las'

# Read the LAZ file
las = pylas.read(laz_file_path)

# Read the .laz file with laspy
with laspy.open(laz_file_path) as laz_file:
    las_data = laz_file.read()

# Write it to a LAS file
las.write(las_file_path)
