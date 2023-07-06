from utility. drawroi import PolygonDrawer
from utility.image import drawRoi
from utility.pointTest import is_point_inside_polygon

from yolov7 import detect

import cv2
import numpy as np
import threading
import queue
import time

class VideoCaptureThread(threading.Thread):
    def __init__(self, camera_id, frame_queue):
        threading.Thread.__init__(self)
        self.camera_ip = camera_id
        self.capture = cv2.VideoCapture(self.camera_ip)
        self.frame_queue = frame_queue
        self.running = True
        self.change = False
        
    def run(self):
        while self.running:
            ret,frame = self.capture.read()
            if not ret:
                print('video not found')
                break
            
            #remove previous frame
            while self.frame_queue.qsize() > 1:
                self.frame_queue.get()
            
            self.frame_queue.put(frame)
            time.sleep(0.033)
            
        self.capture.release()
        
    def stop(self):
        self.running = False
        self.join()

def main():
    yolov7 = detect()
    filename = './video/raw_loitering.mp4'
    cap = cv2.VideoCapture(filename)
    _, frame = cap.read()
    roi = PolygonDrawer(frame)
    cap.release()
    
    roiCoordinate = roi.draw_roi()
    
    the_queue = queue.Queue(maxsize=2)
    
    threads = [
        VideoCaptureThread(filename, the_queue)
    ]
    
    for thread in threads:
        thread.start()
        
    while True:
        frame = the_queue.get()
        
        frame, _ = yolov7.predict(frame)
        frame = drawRoi(frame, np.asarray(roiCoordinate))
        cv2.imshow("loitering video", frame)
        if cv2.waitKey(1) == ord('q'):
            break
        
    for thread in threads:
        thread.stop()

    return

if __name__ == "__main__":
    main()