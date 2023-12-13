import pyautogui
import time
time.sleep(3)
for i in range(9):
    pyautogui.typewrite("Spam")
    pyautogui.press("enter")
    time.sleep(4)
    