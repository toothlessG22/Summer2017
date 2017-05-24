import pyautogui
import time
import openCVLocate

def lockIn(champs):
    images = []
    for champ in champs:
        if champ == 'ashe':
            images.append('img/ashe.PNG')
        elif champ == 'jhin':
            images.append('img/jhin.PNG')
        elif champ == 'vayne':
            images.append('img/vayne.PNG')
        else:
            images.append('img/ashe.PNG')

    location = None

    while location == None:
        for image in images:
            tmploc = openCVLocate.locateCenter(image)
            if tmploc is not None:
                location = tmploc
        time.sleep(.3)

    pyautogui.click(location, duration=.07)

    time.sleep(.7)
    while openCVLocate.locateCenter('img/lockIn.png') == None:
        time.sleep(.3)
    while openCVLocate.locateCenter('img/lockIn.png') is not None:
        pyautogui.click(openCVLocate.locateCenter('img/lockIn.png'), duration=.2)
        time.sleep(5)

if __name__ == "__main__":
    lockIn('ashe')