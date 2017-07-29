# Using DepthSense 325 with Python
# ====== Description ======
These files let you extract data from the DepthSense 325 including the colorMap, depthMap, confidenceMap, vertices and uvMap.

# ====== Dependencies ======
NumPy
> pip install numpy

OpenCV
> pip install opencv-python

Matplotlib
> pip install matplotlib

DepthSense 325 SDK
> Download SDK from https://www.softkinetic.com/support/download

# ====== Steps ======
1. Download this repository in $HOME and run the following commands:

> cd $HOME/DepthSense_325

> python setup.py install

> sudo cp $HOME/DepthSense_325/softkinetic.conf /etc/ld.so.conf.d 

> sudo ldconfig

Note: If the repo is not in the $HOME directory, edit the second line in softkinetic.conf.

2. Run the python script:

> python depthsense_grabber.py
