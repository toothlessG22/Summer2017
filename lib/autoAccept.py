import time
import pyautogui

if __name__ == "__main)":
    import openCVLocate
    imgpath = "../img"
else:
    from lib import openCVLocate
    imgpath = "img"

def autoAccept():
    delay = 7
    accepted = False
    while True:
        print("accepting")
        if(openCVLocate.locateCenter(imgpath + '/accept.PNG') != None):
            acceptCoords = openCVLocate.locateCenter(imgpath + '/accept.PNG')
            pyautogui.click(acceptCoords, duration=.1)
            pyautogui.click(acceptCoords[0], acceptCoords[1]-50, duration=.5)
            accepted = True
            delay = 1

        if(accepted and openCVLocate.locateCenter(imgpath + '/wardInChampSelect.PNG')):
            break

        time.sleep(delay)

if __name__ == "__main__":
    autoAccept()