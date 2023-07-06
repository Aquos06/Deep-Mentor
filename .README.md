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

## To do :white_check_mark:
- [ ] Give 3 frame threshold
- [ ] Change deleteId in Loitering class
- [ ] Output the json
- [ ] Give comments

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