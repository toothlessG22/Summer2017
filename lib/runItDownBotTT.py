import time
import pyautogui

if __name__ == "__main__":
    import keyHelper, openCVLocate
    imgpath = "../img"
else:
    from lib import keyHelper, openCVLocate
    imgpath = "img"

def runitdownbot(team):
    time.sleep(5)
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

    cloop = 0

    while True:
        cloop += 1
        ctime = time.clock()
        try:
            if (cloop + 3) % 15 == 0:
                dodgeBack(BTcoords)
            if cloop % 15 == 0:
                autoItDown(BTcoords)
        finally:
            time.sleep(max(.7 - (time.clock() - ctime), 0))

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