import os
import random
import time

try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui

screen_width, screen_height = pyautogui.size()

while True:
    # Move the mouse cursor randomly
    x_offset = random.randint(0, screen_width)
    y_offset = random.randint(0, screen_height)
    base_duration = abs(x_offset/screen_width)+abs(y_offset/screen_height)
    duration = random.uniform(base_duration*0.5, base_duration*2)

    # Uncomment this to disable the fail-safe
    # pyautogui.FAILSAFE = False

    pyautogui.moveTo(x_offset, y_offset, duration=duration, tween=pyautogui.easeInOutQuad)
    # time.sleep(random.random())
