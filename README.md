# RearViewCameraSimulation

## Rear view camera simulation with guidelines and object detection

### Dependencies:
* numpy
* opencv
* yaml

### Assumptions:
* The world coordinate frame perfectly aligns with the camera frame.
* The camera using which the video has been captured doesn't have any radial or tangential distortion.

### File to run:
sim.py: This is the main file which performs the simulation by taking the following user inputs while runtime. The simulation is a linear change in the steering wheel from zero degrees to the user input angle in degrees.

![userinputs](images/userinputs.png)

### Details of Files:

* ##### params.yaml
    Before running the simulation ensure that the details provided in this file are correct and plausible.

* ##### parser.py
    This file consists of the helper functions to parse the config file and input video file.
    
* #### transform.py
    This files has the transformation funciton to transform from 3d coordinates to 2d image plane.

### Output:
The outut is the simulation window with the guidelines changing according to the steering wheel angle.

### Dependencies:
* highway_env
* gymnasium
* scipy
* opencv

### Note:
Object detection task is WIP.
