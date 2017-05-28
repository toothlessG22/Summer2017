import time
import pyautogui

if __name__ == "__main)":
    import openCVLocate
    imgpath = "../img"
else:
    from lib import openCVLocate
    imgpath = "img"

def clickX():
    while openCVLocate.locateCenter(imgpath + '/X.PNG', thold=.95) is None:
        pos = openCVLocate.locateCenter(imgpath + '/OK.PNG', thold=.65)
        if pos is not None:
            print('see OK')
            pyautogui.click(pos, duration=.6)
            pyautogui.moveTo(x=pos[0], y=pos[1]+40)
        time.sleep(1)

    time.sleep(10)
    while openCVLocate.locateCenter(imgpath + '/X.PNG', thold=.95) is not None:
        pos = openCVLocate.locateCenter(imgpath + '/OK.PNG', thold=.65)
        if pos is not None:
            pyautogui.click(pos, duration=.6)
            pyautogui.moveTo(x=pos[0], y=pos[1] + 40)
        time.sleep(2)
        pyautogui.click(openCVLocate.locateCenter(imgpath + '/X.PNG'))
        time.sleep(2)
        pos = openCVLocate.locateCenter(imgpath + '/OK.PNG', thold=.65)
        if pos is not None:
            pyautogui.click(pos, duration=.6)
            pyautogui.moveTo(x=pos[0], y=pos[1] + 40)

if __name__ == "__main__":
    clickX()