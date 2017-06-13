import time
import pyautogui
import math
from PIL import ImageGrab, Image
import numpy as np

if __name__ == "__main__":
    import keyHelper, openCVLocate, buyUpgradeAndBack
    imgpath = "../img"
else:
    from lib import keyHelper, openCVLocate, buyUpgradeAndBack
    imgpath = "img"

buyorder = [
        1,
        ["blade", 450],
        ["boot", 50],
        ["potion", 50],
        ["potion", 50],
        ["zeal", 1200],
        ["bf",1300],
        ["runaan", 1400],
        ["vampi", 900],
        ["bloodthirs", 1500],
        ["bers", 1100],
        ["bf", 1300],
        ["infi", 2100],
        ["zeal", 1200],
        ["phan", 1400],
        ["vampi", 900],
        ["mercuri", 2700]
    ]


def runitdownbot(team):
    time.sleep(1)

    T = time.clock()
    # assume loaded
    # click in screen
    BTcoords = None
    if (team == "blue"):
        while BTcoords is None:
            BTcoords = openCVLocate.locateCenter(imgpath + '/blueTeamTT.PNG')
    else:
        BTcoords = None
    clickInGame(BTcoords)

    im = np.array(ImageGrab.grab().convert('RGB'))
    buyUpgradeAndBack.buy(buyorder, im, BTcoords, xoff=-296, yoff=70)
    cloop = 0

    while True:
        cloop += 1
        ctime = time.clock()

        im = np.array(ImageGrab.grab().convert('RGB'))
        health = getHealth(im, BTcoords)
        print("H:" + str(health))

        if health is 0:
            buyUpgradeAndBack.buy(buyorder, im, BTcoords, xoff=-296, yoff=70)
        elif health < .2:
            buyUpgradeAndBack.buy(buyorder, im, BTcoords, xoff=-296, yoff=70)

        if (cloop + 2) % 10 == 0:
            dodgeBack(BTcoords)
        if cloop % 10 == 0:
           autoItDown(BTcoords)
        time.sleep(max(.7 - (time.clock() - ctime), 0))

def getHealth(im, BTcoords):
    y = math.floor(BTcoords[1]) + 67
    x = math.floor(BTcoords[0]) - 672
    healthBarImgArray = im[y:y + 2, x:x + 293]
    Image.fromarray(healthBarImgArray).save('t4.png')
    healthPercent = 0
    for i in range(292, 0, -1):
        if (int(healthBarImgArray[0][i][0]) + int(healthBarImgArray[0][i][1]) + int(
                healthBarImgArray[0][i][2]) > 175):
            healthPercent = i / 293
            break
    return healthPercent*100

def dodgeBack(BTcoords):
    pyautogui.moveTo(BTcoords[0] - 1000, BTcoords[1]-300, duration=.2)
    pyautogui.click(BTcoords[0] - 1000, BTcoords[1] - 300, duration=.2, button='right')
    pyautogui.mouseUp(BTcoords[0] - 1000, BTcoords[1] - 300, duration=.2, button='right')

def clickInGame(imageCoords):
    pyautogui.moveTo(imageCoords, duration=2)
    pyautogui.click(imageCoords, duration=.2)
    pyautogui.mouseUp(imageCoords, duration=.1)

def autoItDown(BTcoords):
    off = 0
    keyHelper.PressKey(0x1E)
    pyautogui.moveTo(BTcoords[0] - off, BTcoords[1] + off, duration=.4)
    time.sleep(.2)
    pyautogui.click(BTcoords[0] - off, BTcoords[1] + off, clicks=1, button='left', duration=.1)
    time.sleep(.2)
    pyautogui.mouseUp(button='left')
    time.sleep(.2)
    keyHelper.ReleaseKey(0x1E)

if __name__ == "__main__":
    runitdownbot("blue")