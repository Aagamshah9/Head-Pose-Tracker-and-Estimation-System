import numpy as np

def ref3DModel():
    modelPoints = [[0.0, 0.0, 0.0],
                   [0.0, -330.0, -65.0],
                   [-225.0, 170.0, -135.0],
                   [225.0, 170.0, -135.0],
                   [-150.0, -150.0, -125.0],
                   [150.0, -150.0, -125.0]]
    return np.array(modelPoints, dtype=np.float64)


def ref2dImagePoints(shape):
    imagePoints = [[shape.part(30).x, shape.part(30).y],  # Nose Tip
                   [shape.part(8).x, shape.part(8).y],    # Chin
                   [shape.part(36).x, shape.part(36).y],  # Left Eye left corner
                   [shape.part(45).x, shape.part(45).y],  # Right eye right corner
                   [shape.part(48).x, shape.part(48).y],  # Left mouth corner
                   [shape.part(54).x, shape.part(54).y]]  # Right mouth corner
    return np.array(imagePoints, dtype=np.float64)


def cameraMatrix(fl, center):
    mat = [[fl, 1, center[0]],
                    [0, fl, center[1]],
                    [0, 0, 1]]
    return np.array(mat, dtype=np.float)
