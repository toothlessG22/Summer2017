import time
import pyautogui

if __name__ == "__main)":
    import openCVLocate
    imgpath = "../img"
else:
    from lib import openCVLocate
    imgpath = "img"

def clickX():
    OKCount = 0
    while openCVLocate.locateCenter(imgpath + '/OK.PNG') == None:
        OKCount+=1
        print("dont see OK")
        time.sleep(5)
        if(OKCount > 6):
            break
    if(openCVLocate.locateCenter(imgpath + '/OK.PNG') is not None):
        print('see OK')
        pyautogui.click(openCVLocate.locateCenter(imgpath + '/OK.PNG'))

    while(openCVLocate.locateCenter(imgpath + '/X.PNG') == None):
        print('dont see X')
        time.sleep(5)
    pyautogui.click(openCVLocate.locateCenter(imgpath + '/X.PNG'))

if __name__ == "__main__":
    clickX()