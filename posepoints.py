#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import cv2
import numpy as np

def get_2d_points(image, rotation_vector, translation_vector, camera_matrix, val):
    """Return the 3D points present as 2D for making annotation box"""
    point_3d = []
    dist_coeffs = np.zeros((4,1))
    rear_size = val[0]
    rear_depth = val[1]
    point_3d.append((-rear_size, -rear_size, rear_depth))
    point_3d.append((-rear_size, rear_size, rear_depth))
    point_3d.append((rear_size, rear_size, rear_depth))
    point_3d.append((rear_size, -rear_size, rear_depth))
    point_3d.append((-rear_size, -rear_size, rear_depth))
    
    front_size = val[2]
    front_depth = val[3]
    point_3d.append((-front_size, -front_size, front_depth))
    point_3d.append((-front_size, front_size, front_depth))
    point_3d.append((front_size, front_size, front_depth))
    point_3d.append((front_size, -front_size, front_depth))
    point_3d.append((-front_size, -front_size, front_depth))
    point_3d = np.array(point_3d, dtype=np.float).reshape(-1, 3)
    
    # Map to 2D image points
    (point_2d, _) = cv2.projectPoints(point_3d,rotation_vector,translation_vector,camera_matrix,dist_coeffs)
    point_2d = np.int32(point_2d.reshape(-1, 2))
    return point_2d

    
    
def head_pose_points(image, rotation_vector, translation_vector, camera_matrix):
    """
    Get the points to estimate head pose sideways    

    Parameters
    ----------
    image : np.unit8
            Original Image.
    rotation_vector : Array of float64
                      Rotation Vector obtained from cv2.solvePnP
    translation_vector : Array of float64
                         Translation Vector obtained from cv2.solvePnP
    camera_matrix : Array of float64
                    The camera matrix

    Returns
    -------
    (x, y) : tuple
             Coordinates of line to estimate head pose

    """
    rear_size = 1
    rear_depth = 0
    front_size = image.shape[1]
    front_depth = front_size*2
    val = [rear_size, rear_depth, front_size, front_depth]
    point_2d = get_2d_points(image, rotation_vector, translation_vector, camera_matrix, val)
    y = (point_2d[5] + point_2d[8])//2
    x = point_2d[2]
    
    return (x, y)

