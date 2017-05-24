import pyautogui
import time
import openCVLocate

def clickX():
    OKCount = 0
    while openCVLocate.locateCenter('img/OK.PNG') == None:
        OKCount+=1
        time.sleep(5)
        if(OKCount > 6):
            break
    pyautogui.click(openCVLocate.locateCenter('img/OK.PNG'))

    while(openCVLocate.locateCenter('img/X.PNG') == None):
        time.sleep(5)

    pyautogui.click(openCVLocate.locateCenter('img/X.PNG'))

if __name__ == "__main__":
    clickX()