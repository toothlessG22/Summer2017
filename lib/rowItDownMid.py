import time
import pyautogui
import numpy as np
from PIL import ImageGrab
import math

if __name__ == "__main__":
    import keyHelper, openCVLocate, OCR, buyUpgradeAndBack
    imgpath = "../img"
else:
    from lib import keyHelper, openCVLocate, OCR, buyUpgradeAndBack
    imgpath = "img"

buyorder = [
        1,
        ["blade", 450],
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

upgradeorder = [
        1,
        'q',
        'w',
        'e',
        'w',
        'w',
        'r',
        'w',
        'w',
        'q',
        'q',
        'r',
        'q',
        'q',
        'e',
        'e',
        'r',
        'e',
        'e'
    ]

def rowdownmid(team):
    time.sleep(5)
    T = time.clock()
    # assume loaded
    # click in screen
    BTcoords = None
    if (team == "blue"):
        while BTcoords is None:
            BTcoords = openCVLocate.locateCenter(imgpath + '/blueTeam.PNG')
    else:
        BTcoords = None

    clickInGame(BTcoords)
    # press y to lock camera
    keyHelper.PandRKey(keyHelper.cToHex('y'))
    # buy dorans blade
    screenshotArray = np.array(ImageGrab.grab().convert('RGB'))
    buyUpgradeAndBack.buy(buyorder, screenshotArray, BTcoords)

    cloop = 0
    lastHealth = 0

    time.sleep(40)
    # main loop
    # move back on big damage
    # remove slow move
    # make the loop[ faster for back and forth
    # buy on back
    # back on low health
    # level all abilities
    # use all abilities in a forward direction
    while True:
        cloop += 1
        ctime = time.clock()
        screenshotArray = np.array(ImageGrab.grab().convert('RGB'))
        try:
            health = int(OCR.getWhiteText(screenshotArray, math.floor(BTcoords[0] - 545), 26, math.floor(BTcoords[1] + 120), 12, lower=150).replace('.', '').replace(' ', ''))
            if (health == 0):
                dead(screenshotArray, BTcoords)
                continue
            elif health < 200:
                keyHelper.PandRKey(keyHelper.cToHex('f'))
                buyUpgradeAndBack.back(buyorder, screenshotArray, BTcoords)
                continue
            if(health - lastHealth < -130):
                moveBackwards(1, BTcoords)
                autoDownMid(BTcoords, time.clock() - T)
            if(openCVLocate.locateCenter(imgpath + '/upgrade.PNG') is not None):
                buyUpgradeAndBack.upgrade()
            if cloop % 10 == 0:
                autoDownMid(BTcoords, time.clock() - T)

            print(health)
            lastHealth = health
        except ValueError:
            print("health got messed up")
        finally:
            time.sleep(max(.7 - (time.clock() - ctime), 0))

def clickInGame(imageCoords):
    pyautogui.moveTo(imageCoords, duration=2)
    pyautogui.click(imageCoords, duration=.2)
    pyautogui.mouseUp(imageCoords, duration=.1)

def dead(screenshot, BTcoords):
    buyUpgradeAndBack.buy(buyorder, screenshot, BTcoords)

def moveBackwards(steps, BTcoords):
    print("moving backwards " + str(steps) + "step(s)")
    for cstep in range(steps):
        pyautogui.moveTo(BTcoords[0]-800, BTcoords[1], duration=.05)
        pyautogui.click(BTcoords[0]-800, BTcoords[1], button='right', duration=.1)
        time.sleep(.2)
        pyautogui.mouseUp(button='right')
        time.sleep(2.3)

def autoDownMid(BTcoords, T):
    if T/60 < 6:
        off = 48
    elif T/60 < 11:
        off = 25
    else:
        off = -10

    keyHelper.PressKey(0x1E)
    pyautogui.moveTo(BTcoords[0] - off, BTcoords[1] + off, duration=.4)
    time.sleep(.2)
    pyautogui.click(BTcoords[0] - off, BTcoords[1] + off, clicks=1, button='left', duration=.1)
    time.sleep(.2)
    pyautogui.mouseUp(button='left')
    time.sleep(.2)
    keyHelper.ReleaseKey(0x1E)

def use(key, BTcoords):
    pyautogui.moveTo(BTcoords[0], BTcoords[1]-550, duration=.3)
    keyHelper.PandRKey(keyHelper.cToHex(key))

if __name__ == "__main__":
    rowdownmid("blue")
