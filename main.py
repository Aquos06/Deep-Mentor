import cv2
import numpy as np

class PolygonDrawer:
    def __init__(self, image):
        self.image = image
        self.drawing = False
        self.polygon_completed = False
        self.points = []
        self.finished = False

    def draw_polygon(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.points.append((x, y))
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
        elif event == cv2.EVENT_RBUTTONUP:
            self.polygon_completed = True

    def draw_roi(self):
        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image", self.draw_polygon)

        image_copy = self.image.copy()
        while True:

            if len(self.points) > 0 and not self.finished:
                cv2.polylines(image_copy, np.array([self.points]), False, (0, 255, 0), 2)

            cv2.imshow("Image", image_copy)

            if self.polygon_completed:
                image_copy = cv2.polylines(image_copy, np.array([self.points]), True, (0,255,0), 2)
                self.finished = True
                self.polygon_completed = False

            key = cv2.waitKey(1) & 0xFF
            if key == 13:  # Press Esc key to exit
                break

        cv2.destroyAllWindows()
        return self.points

def main():
    # Load image
    image_path = "test.png"
    image = cv2.imread(image_path)

    # Create a PolygonDrawer instance
    drawer = PolygonDrawer(image)

    # Call the draw_roi method
    drawer.draw_roi()

if __name__ == "__main__":
    main()