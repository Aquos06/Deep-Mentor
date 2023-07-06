from utility.pointTest import is_point_inside_polygon

from datetime import datetime
import numpy as np

class Loitering:
    def __init__(self):
        self.storage = {}
        self.deleteId = []
        #TODO: give 3 frame threshold to say that he is outside the frame
        #TODO: change deleteId, bcs if he go out and in again cannot count
        
    def check(self, roiCoordinate, personCoordinate):
        returnCoordinate = []
        timeNow = datetime.now()
        for i in personCoordinate:
            midLeg = self.xyxy2bot(i)
            
            if is_point_inside_polygon(np.asarray(roiCoordinate), midLeg):
                print("is inside")
                if i[-1] not in self.storage and i[-1] not in self.deleteId:
                    newData = {
                        i[-1] : {
                            "timeIn": datetime.now()
                        }
                    }
                    self.storage.update(newData)
                if i[-1]not in self.deleteId:
                    timeDifference = timeNow - self.storage[i[-1]]['timeIn']
                    if timeDifference.total_seconds() >=5 :
                        self.deleteId.append(i[-1])
                        del self.storage[i[-1]]
                        returnCoordinate.append(i)
            else:
                if i[-1] in self.storage:
                    del self.storage[i[-1]]
                    
                    
        return timeNow, returnCoordinate
    
    def xyxy2bot(self, coordinate):
        x1,_,x2,y2,_,_ = coordinate
        midLeg= [x1 + ((x2-x1)/2),y2]
        
        return midLeg
                    