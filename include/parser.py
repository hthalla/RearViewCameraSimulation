"""
Created on Mon Nov 28 10:48:24 EST 2023

@author: Prasanna Gupta

Description: This is the utils file with parser functions.
"""

import cv2
import yaml


def parse_yaml_file(filepath: str):
    """
        Parsing the yaml file.
    """
    with open(filepath, 'r') as file:
        params = yaml.safe_load(file)

    return params

def parse_video(videopath: str):
    """
        Parsing the video file path.
    """
    capture = cv2.VideoCapture(videopath)

    return capture
