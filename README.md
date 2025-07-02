# 🖱️ Auto Image Clicker and Scroller

A Python script that continuously scrolls and waits to detect a target image on screen—when the image appears, it automatically clicks it.  
Ideal for automating repetitive click‑and‑scroll workflows.

## 📌 Features

- **Smooth Scrolling**: Continuously scrolls by a fixed amount at a set speed.
- **Image Detection & Click**: Looks for `target_image.png` on your screen (with adjustable confidence) and clicks on its center.
- **Threaded Operation**: Runs scrolling, detection, and “press q to quit” listener in parallel threads.
- **Graceful Exit**: Press `q` at any time to stop all threads.

## Prerequisites

- Python 3.7+  
- `target_image.png` placed in the same folder as the script.


## 🎯 How It Works

- Continuously scrolls the screen at the mouse position.
- Continuously checks for a specific image (`target_image.png`) on the screen.
- Automatically clicks the image when found.

## ⚙️ Requirements

This script uses the following Python libraries:
- `pyautogui`
- `keyboard`
- `opencv-python`
-  On some systems, pyautogui may require additional permissions or dependencies (like pillow for image processing). `pillow`
-  ```bash
   pip install Pillow
   ```

### 1. Clone the repository:

```bash
git clone https://github.com/AkshitKdhaka/Auto-Image-Clicker-and-Scroller.git
cd AutoImageClickerScroller
```
### 2. Install Dependencies
   
## 📥 Installation
Option 1: Install all Using requirements.txt (recommended):
```bash
pip install -r requirements.txt
```

Option 2: Install all libraries one time :
```bash
pip install pyautogui keyboard Pillow opencv-python
```

Option 3: Install libraries one by one:
```bash
pip install pyautogui
pip install Pillow
pip install keyboard
pip install opencv-python
```

### 3. Add Your Image
Place the image you want to detect in the same folder and update the image path in the script:
```
IMAGE_PATH = r'target_image.png'
```

### 4. Run the Script
After installing all the library run the script:
```bash
python "Auto image clicker and scroller.py"

