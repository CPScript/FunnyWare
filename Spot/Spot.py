import os
from os import system
os.system('pip install pyautogui')
import pyautogui


pixel_data = [(0, 0, 0)] 
pixel_image = pyautogui.Image(pixel_data, size=(1, 1))

pyautogui.mouse.Cursor(pixel_image)

pyautogui.sleep(10)
