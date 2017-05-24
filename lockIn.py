import pyautogui
import time
import openCVLocate

def lockIn(champ):
    if champ == 'ashe':
        image = 'img/ashe.PNG'
    else:
        image = 'img/ashe.PNG'
    while openCVLocate.locateCenter(image) == None:
        time.sleep(.3)
    pyautogui.click(openCVLocate.locateCenter(image), duration=.07)

    time.sleep(.7)
    while openCVLocate.locateCenter('img/lockIn.png') == None:
        time.sleep(.3)
    pyautogui.click(openCVLocate.locateCenter('img/lockIn.png'), duration=.2)

if __name__ == "__main__":
    lockIn('ashe')