import pyautogui
import time

def lockIn(champ):
    if champ == 'ashe':
        image = 'img/ashe.PNG'
    else:
        image = 'img/ashe.PNG'
    while pyautogui.locateCenterOnScreen(image) == None:
        time.sleep(.3)
    pyautogui.click(pyautogui.locateCenterOnScreen(image), duration=.07)

    time.sleep(.7)
    while pyautogui.locateCenterOnScreen('img/lockIn.png') == None:
        time.sleep(.3)
    pyautogui.click(pyautogui.locateCenterOnScreen('img/lockIn.png'), duration=.2)

if __name__ == "__main__":
    lockIn('ashe')