import pyautogui
import time

def autoAccept():
    delay = 7
    accepted = False
    while True:
        print("accepting")
        if(pyautogui.locateCenterOnScreen('img/accept.PNG') != None):
            acceptCoords = pyautogui.locateCenterOnScreen('img/accept.PNG')
            pyautogui.click(acceptCoords, duration=.1)
            pyautogui.click(acceptCoords[0], acceptCoords[1]-50, duration=.5)
            accepted = True
            delay = 1

        if(accepted and pyautogui.locateCenterOnScreen('img/wardInChampSelect.PNG')):
            break

        time.sleep(delay)

if __name__ == "__main__":
    autoAccept()