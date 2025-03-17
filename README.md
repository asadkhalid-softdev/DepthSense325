# DepthSense 325 Python Integration

## Overview

This package provides Python bindings for the DepthSense 325 camera, allowing you to extract various data streams including color maps, depth maps, confidence maps, vertices, and UV maps. The integration enables computer vision and depth sensing applications using Python.

## Installation

### Prerequisites

Before installing, ensure you have the following dependencies:

- **Python Libraries**:
    - NumPy: `pip install numpy`
    - OpenCV: `pip install opencv-python`
    - Matplotlib: `pip install matplotlib`
- **DepthSense 325 SDK**:
    - Download from the SoftKinetic support website
    - Follow the SDK installation instructions for your platform


### Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/asadkhalid-softdev/DepthSense_325.git
cd DepthSense_325
```

2. Install the Python package:

```bash
python setup.py install
```

3. Configure system libraries:

```bash
sudo cp softkinetic.conf /etc/ld.so.conf.d/
sudo ldconfig
```

> **Note**: If you cloned the repository to a location other than your home directory, edit the path in `softkinetic.conf` accordingly.

## Usage

Run the example script to verify your installation:

```bash
python depthsense_grabber.py
```

This will initialize the camera and display the various data streams.

## Example Code

```python
import depthsense as ds

# Initialize the camera
context = ds.Context()
camera = context.get_device()

# Configure camera parameters
camera.enable_depth(ds.DepthMode.QVGA)
camera.enable_color(ds.ColorMode.HD720)

# Start capturing
context.start_capture()

# Get frames
depth_frame = camera.get_depth_frame()
color_frame = camera.get_color_frame()

# Process data
depth_map = depth_frame.get_depth_map()
color_map = color_frame.get_color_map()
```


## Documentation

For more detailed information about the API and usage examples, refer to the documentation in the `docs/` directory.

## Troubleshooting

- Ensure the camera is properly connected via USB 3.0
- Verify that the SDK is correctly installed
- Check system permissions for USB device access


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- SoftKinetic for providing the DepthSense SDK
- Contributors to the Python wrapper

For a video tutorial, visit: [DepthSense 325 Python Tutorial](https://www.youtube.com/watch?v=G95gE5XfCho&t=51s)

<div style="text-align: center">⁂</div>

[^1]: https://www.youtube.com/watc

