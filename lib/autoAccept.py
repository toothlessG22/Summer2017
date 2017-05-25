import time

import pyautogui

from lib import openCVLocate


def autoAccept():
    delay = 7
    accepted = False
    while True:
        print("accepting")
        if(openCVLocate.locateCenter('../img/accept.PNG') != None):
            acceptCoords = openCVLocate.locateCenter('../img/accept.PNG')
            pyautogui.click(acceptCoords, duration=.1)
            pyautogui.click(acceptCoords[0], acceptCoords[1]-50, duration=.5)
            accepted = True
            delay = 1

        if(accepted and openCVLocate.locateCenter('../img/wardInChampSelect.PNG')):
            break

        time.sleep(delay)

if __name__ == "__main__":
    autoAccept()