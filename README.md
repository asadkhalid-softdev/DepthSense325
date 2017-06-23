# DepthSense_325
# ====== Description ======
These files let you extract data from the DepthSense 325 including the colorMap, depthMap, confidenceMap, vertices and uvMap.

# ====== Requirements ======
NumPy, OpenCV, Matplotlib

# ====== Steps ======
1. Download this repository in $HOME and run the following commands:

>> cd /home/DepthSense_325
>> python setup.py install
>> sudo cp /home/DepthSense_325/softkinetic.conf /etc/ld.so.conf.d 

Note: If the repo is not in the $HOME directory, edit the second line in softkinetic.conf.

2. Run the python script:

>> python depthsense_grabber.py
