"""
Created on Mon Nov 28 10:48:24 EST 2023

@author: Prasanna Gupta

Description: This is the utils file with 3d to 2d transformation functions.
"""

import cv2
import numpy as np


def transform_3d_to_2d(img, center, radius1, radius2, scaling_factor, heading):
    """
        Project curve on the 2d image.
    """
    # Extracting height of the image
    height = img.shape[0]
    width = img.shape[1]

    # Generating linear coordinates of the left wheel
    theta = np.linspace(0, np.pi/2, 5000)
    if heading > 0:
        x = center[0] - radius1 * np.cos(theta)
        y = center[1] - radius1 * np.sin(theta)
    else:
        x = width - center[0] + radius2 * np.cos(theta)
        y = center[1] - radius2 * np.sin(theta)

    # Transforming the coordinates
    points = np.column_stack((x, y))
    points[:,0] = points[:,0] + (height-points[:,1])*100*scaling_factor/height
    points[:,1] = height - (height-points[:,1])/scaling_factor
    points = points[points[:, 1] > height/2]
    points = points.astype(int)

    # Projecting on to the 2d image
    cv2.polylines(img, [points], isClosed=False, color=(0, 255, 0), thickness=3)

    # Generating linear coordinates of the right wheel
    if heading > 0:
        x = center[0] - radius2 * np.cos(theta)
        y = center[1] - radius2 * np.sin(theta)
    else:
        x = width - center[0] + radius1 * np.cos(theta)
        y = center[1] - radius1 * np.sin(theta)

    # Transforming the coordinates
    points = np.column_stack((x, y))
    points[:,0] = points[:,0] - (height-points[:,1])*100*scaling_factor/height
    points[:,1] = height - (height - points[:,1])/scaling_factor
    points = points[points[:, 1] > height/2]
    points = points.astype(int)

    # Projecting on to the 2d image
    cv2.polylines(img, [points], isClosed=False, color=(0, 255, 0), thickness=3)

    return img


def max_transform_3d_to_2d(img, center, max_turning_radius, scaling_factor):
    """
        Project max curve on the 2d image.
    """
    # Extracting height of the image
    height = img.shape[0]
    width = img.shape[1]

    # Generating linear coordinates of the left wheel
    theta = np.linspace(0, np.pi/2, 5000)
    x = center[0] - max_turning_radius * np.cos(theta)
    y = center[1] - max_turning_radius * np.sin(theta)

    # Transforming the coordinates
    points = np.column_stack((x, y))
    points[:,0] = points[:,0] + (height-points[:,1])*100*scaling_factor/height
    points[:,1] = height - (height-points[:,1])/scaling_factor
    points = points[points[:, 1] > height/2]
    points = points.astype(int)

    # Projecting on to the 2d image
    cv2.polylines(img, [points], isClosed=False, color=(0, 0, 255), thickness=3)

    # Generating linear coordinates of the right wheel
    x = width - center[0] + max_turning_radius * np.cos(theta)
    y = center[1] - max_turning_radius * np.sin(theta)

    # Transforming the coordinates
    points = np.column_stack((x, y))
    points[:,0] = points[:,0] - (height-points[:,1])*100*scaling_factor/height
    points[:,1] = height - (height - points[:,1])/scaling_factor
    points = points[points[:, 1] > height/2]
    points = points.astype(int)

    # Projecting on to the 2d image
    cv2.polylines(img, [points], isClosed=False, color=(0, 0, 255), thickness=3)

    return img
