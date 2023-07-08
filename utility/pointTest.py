import cv2

def is_point_inside_polygon(roi,point):
    """
    Check if the point inside the ROI
    Input: 
        roi: ROI's coordinate
        point: person coordiante [x1,y1,x2,y2, cid, personId]
    Output:
        True, False
    """ 
    result = cv2.pointPolygonTest(roi, point, False)
    if result > 0:
        return True
    else:
        return False