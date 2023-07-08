from utility.pointTest import is_point_inside_polygon

from datetime import datetime
import numpy as np

class Loitering:
    """
        To find the loitering event
    """
    def __init__(self):
        self.storage = {}
        self.deleteId = []
        
    def check(self, roiCoordinate, personCoordinate):
        """
            Input: 
                roiCoordinate: ROI's coordinate (list)
                personCoordinate: person yolov7 coordinate (list)
            Output:
                timeNow: time object
                returnCoordinate: the person's coordinate that have loitering event
        """
        returnCoordinate = []
        timeNow = datetime.now()
        for i in personCoordinate:
            midLeg = self.xyxy2bot(i)
            
            if is_point_inside_polygon(np.asarray(roiCoordinate), midLeg):
                if i[-1] not in self.storage and i[-1] not in self.deleteId:
                    newData = {
                        i[-1] : {
                            "timeIn": datetime.now(),
                            "frame threshold": 0
                        }
                    }
                    self.storage.update(newData)
                if i[-1]not in self.deleteId:
                    timeDifference = timeNow - self.storage[i[-1]]['timeIn']
                    self.storage[i[-1]]['frame threshold'] = 0
                    if timeDifference.total_seconds() >=5 :
                        self.deleteId.append(i[-1])
                        del self.storage[i[-1]]
                        returnCoordinate.append(i)
            else:
                if i[-1] in self.storage:
                    self.storage[i[-1]]["frame threshold"] += 1
                    print(self.storage[i[-1]]["frame threshold"])
                    if self.storage[i[-1]]["frame threshold"] >= 5:
                        del self.storage[i[-1]]
                        self.deleteId.remove(i-[-1])
                    
                    
        return timeNow, returnCoordinate
    
    def xyxy2bot(self, coordinate):
        """
        Finding the middle bottem coordinate of the bounding box (middle of the legs)
        Input: 
            coordinate:  bounding box (list) [x1,y1,x2,y2,conf,id]
        Ouput:
            midLeg: x1, y1 (list)
        """
        x1,_,x2,y2,_,_ = coordinate
        midLeg= [x1 + ((x2-x1)/2),y2]
        
        return midLeg
                    