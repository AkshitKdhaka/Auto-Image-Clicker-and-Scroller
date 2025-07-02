import pyautogui
import time
import keyboard
import os
import traceback
import threading  # For running tasks concurrently

# Settings for the scroll
scroll_amount = -100  # Scroll step (negative for down)
scroll_speed = 0.7  # Time delay between scrolls (lower is faster)

# Image path
IMAGE_PATH = r'target_image.png path'  # Make sure this image is in the same folder

# Validate image path
if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"❌ Image file not found at {IMAGE_PATH}. Please check the path.")

# Delay to prevent overloading the system
DELAY_BETWEEN_CHECKS = 0  # seconds

# Shared flag to stop threads
stop_flag = False

def smooth_scroll():
    global stop_flag
    # Get the current position of the mouse
    x, y = pyautogui.position()
    
    while not stop_flag:  # Keep running until stop_flag is True
        pyautogui.scroll(scroll_amount, x, y)  # Scroll down at the current mouse position
        time.sleep(scroll_speed)  # Wait for a short time to make it smooth
    
    print("🛑 Smooth scroll stopped.")

def detect_and_click_image():
    global stop_flag
    print("🚀 Script started! Waiting for the image to appear... Press 'q' to stop.")
    
    try:
        while not stop_flag:
            try:
                # Try locating the image on the screen
                image_location = pyautogui.locateOnScreen(IMAGE_PATH, confidence=0.7)
                
                if image_location:
                    image_center = pyautogui.center(image_location)
                    pyautogui.moveTo(image_center)
                    pyautogui.click()
                    print("✅ Image detected and clicked!")
                    time.sleep(0)  # Pause briefly to avoid rapid re-clicking
                else:
                    print("🔍 Image not found. Still waiting...")
            except pyautogui.ImageNotFoundException:
                print("❌ pyautogui could not find the image on the screen.")
            except Exception as inner_e:
                print(f"❌ An error occurred while locating/clicking the image: {inner_e}")
                traceback.print_exc()  # Print detailed error traceback
            
            time.sleep(DELAY_BETWEEN_CHECKS)
    
    except KeyboardInterrupt:
        print("🛑 Script interrupted manually. Exiting...")
    print("🛑 Image detection stopped.")

def monitor_quit_key():
    global stop_flag
    while not stop_flag:
        if keyboard.is_pressed('q'):  # Check if 'q' is pressed
            print("🛑 'q' key detected. Stopping all tasks...")
            stop_flag = True  # Set the flag to stop other threads
            break

# Create threads for all functions
scroll_thread = threading.Thread(target=smooth_scroll)
image_thread = threading.Thread(target=detect_and_click_image)
quit_thread = threading.Thread(target=monitor_quit_key)

# Start all threads
scroll_thread.start()
image_thread.start()
quit_thread.start()

# Wait for all threads to finish
scroll_thread.join()
image_thread.join()
quit_thread.join()

print("✅ All tasks have been stopped successfully.")
