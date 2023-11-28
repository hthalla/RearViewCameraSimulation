"""
Created on Mon Nov 27 18:45:24 EST 2023

@author: Prasanna Gupta

Description: This is the main file that simulates the rear view camera display with guidelines.
"""
import cv2
import numpy as np

from include.parser import parse_video
from include.parser import parse_yaml_file
from include.transform import transform_3d_to_2d


YAML_FILE_PATH = "config/params.yaml"  # Config file path

if __name__ == "__main__":
    # Parsing the input config file.
    params = parse_yaml_file(YAML_FILE_PATH)
    scaling_factor = int(params["scaling_factor"])
    track_width = int(params["track_width"])
    wheel_base = int(params["wheel_base"])
    steering_ratio = int(params["steering_ratio"])
    max_steering_wheel_angle = int(params["max_steering_wheel_angle"])

    # Parsing the video and its parameters.
    video_path = params["video_path"]
    capture = parse_video(video_path)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Getting user inputs for the simulation.
    heading = int(input("Enter the turn you wish to take (left:1, right:-1): "))
    theta = min(int(input("Enter the steering wheel angle in degrees: ")),
                max_steering_wheel_angle)
    theta = np.linspace(0, theta*np.pi/180, int(frame_count/20))
    turning_radius = wheel_base/(np.tan(theta/steering_ratio+1e-9))/scaling_factor**2

    i=0
    while True:
        # Reading a frame and checking its validity.
        ret, frame = capture.read()
        if not ret:
            break

        if i < int(frame_count/20):
            # Dynamic turning radius calculation of the inner and
            # outer wheel using ackerman geometry
            center = (frame_width + turning_radius[i], frame_height)
            radius1 = frame_width/2 + track_width/2 + turning_radius[i]
            radius2 = frame_width/2 - track_width/2 + turning_radius[i]

            # Projecting the guidelines on the frame
            frame = transform_3d_to_2d(frame, center, radius1, radius2, scaling_factor, heading)

            # Displaying the frame
            cv2.imshow("Rear view camera simulation with guidelines", frame)
            cv2.waitKey(1)
            i += 1