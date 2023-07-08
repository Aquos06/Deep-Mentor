import json

def COCOJSON(project, width, height,filename, coordinate, imageId, categoryId):
    
    coco_dict = {
        "info": {
            "description": project
        },
        "images": [
            {
                "id" : imageId,
                "width": width,
                "height": height,
                "filename": filename
            }
        ],
        "annotations": [
            {
                "id": 0,
                "iscrowd": 0,
                "image_id": imageId,
                "category_id": categoryId,
                "segmentations": coordinate,
                "bbox": get_bounding_box(coordinate),
                "area": get_area(coordinate)
            }
        ],
        "categories": [
            {
                "id": categoryId,
                "name": "alarmzone"
            }
        ]
    }
    path = "./json/roi.json"
    with open(path, "w") as f:
        json.dump(coco_dict, f, indent = 2)
        
def get_bounding_box(coordinate):
    x_values, y_values = zip(*coordinate)
    xmin = min(x_values)
    xmax = max(x_values)
    ymin = min(y_values)
    ymax = max(y_values)
    return [xmin, ymin, xmax - xmin, ymax - ymin]

def get_area(coordinate):
    if len(coordinate) < 3:
        return 0.0

    # Calculate the signed area
    area = 0.0
    n = len(coordinate)
    for i in range(n):
        x1, y1 = coordinate[i]
        x2, y2 = coordinate[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)

    area = abs(area) / 2.0
    
    return area