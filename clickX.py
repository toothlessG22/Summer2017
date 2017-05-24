import pyautogui
import time

def clickX():
    OKCount = 0
    while pyautogui.locateCenterOnScreen('img/OK.PNG') == None:
        OKCount+=1
        time.sleep(5)
        if(OKCount > 6):
            break
    pyautogui.click(pyautogui.locateCenterOnScreen('img/OK.PNG'))

    while(pyautogui.locateCenterOnScreen('img/X.PNG') == None):
        time.sleep(5)

    pyautogui.click(pyautogui.locateCenterOnScreen('img/X.PNG'))

if __name__ == "__main__":
    clickX()