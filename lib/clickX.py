import time

import pyautogui

from lib import openCVLocate

def clickX():
    OKCount = 0
    while openCVLocate.locateCenter('../img/OK.PNG') == None:
        OKCount+=1
        print("dont see OK")
        time.sleep(5)
        if(OKCount > 6):
            break
    if(openCVLocate.locateCenter('../img/OK.PNG') is not None):
        print('see OK')
        pyautogui.click(openCVLocate.locateCenter('../img/OK.PNG'))

    while(openCVLocate.locateCenter('../img/X.PNG') == None):
        print('dont see X')
        time.sleep(5)
    pyautogui.click(openCVLocate.locateCenter('../img/X.PNG'))

if __name__ == "__main__":
    clickX()