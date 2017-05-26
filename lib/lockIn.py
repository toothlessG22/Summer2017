import time

import pyautogui

if __name__ == "__main)":
    import openCVLocate
    imgpath = "../img"
else:
    from lib import openCVLocate
    imgpath = "img"


def lockIn(champs):
    images = []
    for champ in champs:
        if champ == 'ashe':
            images.append(imgpath + '/ashe.PNG')
        elif champ == 'jhin':
            images.append(imgpath + '/jhin.PNG')
        elif champ == 'vayne':
            images.append(imgpath + '/vayne.PNG')
        elif champ == 'varus':
            images.append(imgpath + '/varus.PNG')
        else:
            images.append(imgpath + '/ashe.PNG')

    while openCVLocate.locateCenter('img/lockIn.png', thold=.9) == None:
        for image in images:
            if openCVLocate.locateCenter(image, thold=.9) is not None:
                pyautogui.click(openCVLocate.locateCenter(image, thold=.9))
        time.sleep(5)
    while openCVLocate.locateCenter('img/lockIn.png') is not None:
        pyautogui.click(openCVLocate.locateCenter('img/lockIn.png'), duration=.2)
        for image in images:
            if openCVLocate.locateCenter(image, thold=.9) is not None:
                pyautogui.click(openCVLocate.locateCenter(image, thold=.9))
        time.sleep(5)

if __name__ == "__main__":
    lockIn('ashe')