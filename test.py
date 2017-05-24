import keyHelper
import time
import pyautogui


time.sleep(3)
imageCoords = pyautogui.locateCenterOnScreen('img/blueTeam.PNG')

keyHelper.PressKey(0x1E)
time.sleep(1)
pyautogui.moveTo(imageCoords, duration=1)
pyautogui.click(imageCoords, clicks=1, button='left', duration=.1)
time.sleep(1)
pyautogui.mouseUp(button='left')
time.sleep(.2)
keyHelper.ReleaseKey(0x1E)