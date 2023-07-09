# <p align = "center"> Loitering </p>

## Installation Process :minidisc: 
1. Clone the Repository
```Python
git clone "https://github.com/Aquos06/Deep-Mentor.git"
```
2. Install Depedency
```Python
pip install -r requirements.txt
```
4. Open Folder
```Python
cd Deep-Mentor
```
5. Run the main.py
```Python
python3 main.py
```

## How to Use
1. Run the Program
```Python
python3 main.py
```
2. A window will pop up to draw the ROI
    - Left Click to draw the ROI
    - Right Click to complete the ROI
    - Enter to proceed the ROI drawings

    Draw ROI -> Right Click -> Enter
3. A Video window will pop up and the loitering event monitoring is running

## To do :white_check_mark:
- [X] Give 3 frame threshold
- [X] Change deleteId in Loitering class
- [X] Output the json
- [X] Give comments
- [ ] add How to Use in the README.md
- [ ] add yolov7 and tracking code sources
## File Tree :cactus:
<pre>
.
|--models
|--trackers --> tracker function
|--utility
|  |--drawroi.py
|  |--image.py
|  |--loiteringChecking.py
|  `--pointTest.py
|--video
|--weights
|  `--yolov7.py
|--yolov7Util --> yolov7 utility function
|--README.md
|--main.py --> main file (run this file)
|--track.py
`--yolov7.py --> modified detect.py
</pre>