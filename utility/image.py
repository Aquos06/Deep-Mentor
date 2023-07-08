import cv2
import numpy as np

def drawRoi(image, coordinate):
    """
    Draw ROI in the video 
        Input: 
            Image: image (np.ndarray)
            coordinate: Polygon ROI coordinate (list)
        Output:
            returnImage: image after ROI
    """
    overlay = image.copy()
    
    cv2.fillPoly(overlay, [coordinate], (0,255,0))
    cv2.polylines(image, [coordinate], True, (0,255,0), 2)
    
    returnImage = cv2.addWeighted(image, 1, overlay, 0.3, 0)
    
    return returnImage