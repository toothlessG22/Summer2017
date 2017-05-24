import pyautogui
import time

def waitForLoad():
    while(pyautogui.locateCenterOnScreen('img/blueTeam.png')) == None:
        print("waiting for load")
        time.sleep(5)
    return

def checkTeam():
    if(pyautogui.locateCenterOnScreen('img/blueTeam.png')):
        return 'blue'
    else:
        return 'red'