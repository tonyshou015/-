from pyautogui import *
import payautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if payautogui.locateOnScreen('stickman.png') != None:
        print("i can see it")
        time.sleep(0.5)
    else:
        print("i am unable to see it")
        time.sleep(0.5)
        
