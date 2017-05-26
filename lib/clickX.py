import time
import pyautogui

if __name__ == "__main)":
    import openCVLocate
    imgpath = "../img"
else:
    from lib import openCVLocate
    imgpath = "img"

def clickX():
    while openCVLocate.locateCenter(imgpath + '/X.PNG') is None:
        if(openCVLocate.locateCenter(imgpath + '/OK.PNG') is not None):
            print('see OK')
            pyautogui.click(openCVLocate.locateCenter(imgpath + '/OK.PNG'))

    while openCVLocate.locateCenter(imgpath + '/X.PNG') is not None:
        pyautogui.click(openCVLocate.locateCenter(imgpath + '/OK.PNG'))
        time.sleep(2)
        pyautogui.click(openCVLocate.locateCenter(imgpath + '/X.PNG'))
        time.sleep(2)
        pyautogui.click(openCVLocate.locateCenter(imgpath + '/OK.PNG'))

if __name__ == "__main__":
    clickX()