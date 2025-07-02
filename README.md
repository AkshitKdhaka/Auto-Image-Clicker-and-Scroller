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


### 1. Clone the repository:

```bash
git clone https://github.com/your-username/AutoImageClickerScroller.git
cd AutoImageClickerScroller

## 📥 Installation
Using requirements.txt (recommended)
pip install -r requirements.txt

install libraries one by one:
pip install pyautogui
pip install keyboard
pip install opencv-python


After installing all the library run the script:
python "Auto image clicker and scroller.py"

