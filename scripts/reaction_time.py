from PIL import ImageGrab
import pyautogui
import time
import numpy as np
import keyboard

def get_pixel_color():
    return np.array(ImageGrab.grab().load()[550, 250])
def is_green(mean_color):
    return mean_color[1] > 200

time.sleep(5)
while (not keyboard.is_pressed('b')):
    if (is_green(get_pixel_color())):
        print("GREEN!")
        pyautogui.click()