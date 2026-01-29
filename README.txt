This project uses public LiDAR elevation data from Badlands National Park
and displays it as a matrix of points in max/msp patcher, where (x,y) coords
correspond with downsampled gps coordinates, and (Z) is the elevation.

To run, open Max/MSP patcher, start the jit.world object, and click "import movie" button.
This will open a file explorer with which you should select "Badlands_Heightmap.png".

The rest of this project is basically a means to go from .las file to data formats we can use in Max/MSP.

This is an unpolished jumping off point for getting GPS data into Max/MSP. You could probably do this with a city too.
Maybe hookup an elevation scale factor to RMS of an audio input? Who knows.

Good luck!