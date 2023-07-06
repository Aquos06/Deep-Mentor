import cv2

def is_point_inside_polygon(roi,point):
    result = cv2.pointPolygonTest(roi, point, False)
    if result > 0:
        return True
    else:
        return False