import time
import pyautogui

if __name__ == "__main__":
    import keyHelper, openCVLocate
    imgpath = "../img"
else:
    from lib import keyHelper, openCVLocate
    imgpath = "img"

def rundownmid(team):
    time.sleep(5)
    # main loop
    imageCoords = None
    if (team == "blue"):
        while imageCoords is None:
            imageCoords = openCVLocate.locateCenter(imgpath + '/blueTeam.PNG')
    else:
        imageCoords = None

    pyautogui.moveTo(imageCoords, duration=2)
    pyautogui.click(imageCoords, duration=.1)

    time.sleep(1)

    #buy dorans
    keyHelper.PandRKey(0x19)
    time.sleep(1)
    keyHelper.PressKey(0x1D)  # CTRL
    time.sleep(1)
    keyHelper.PandRKey(0x1C)  # RTRN
    time.sleep(1)
    keyHelper.ReleaseKey(0x1D)  # CTRL

    keyHelper.PandRKey(0x30)  # B
    keyHelper.PandRKey(0x26)  # L
    keyHelper.PandRKey(0x1E)  # A

    time.sleep(.5)

    keyHelper.PandRKey(0x1C) # RTRN
    keyHelper.PandRKey(0x1C) # RTRN

    keyHelper.PandRKey(0x01)  # ESC

    time.sleep(60)

    curr = 0
    while True:
        if curr % 5 == 0:
            print("pressing Q")
            keyHelper.PandRKey(0x10)  # Q
            time.sleep(.5)

        if curr % 24 == 0:
            # buy vamp
            keyHelper.PandRKey(0x19)
            time.sleep(1)
            keyHelper.PressKey(0x1D)  # CTRL
            time.sleep(.4)
            keyHelper.PandRKey(0x1C)  # RTRN
            time.sleep(.4)
            keyHelper.ReleaseKey(0x1D)  # CTRL

            keyHelper.PandRKey(0x2F) #V
            keyHelper.PandRKey(0x1E) #A
            keyHelper.PandRKey(0x32) #M
            keyHelper.PandRKey(0x19) #P
            keyHelper.PandRKey(0x17) #I
            time.sleep(1)
            keyHelper.PandRKey(0x1C)  # RTRN
            keyHelper.PandRKey(0x1C)  # RTRN

            keyHelper.PandRKey(0x01)  # ESC

        if curr % 6 == 0:
            # move to target
            pyautogui.moveTo(x=imageCoords[0]-800, y=imageCoords[1], duration=1)
            pyautogui.click(x=imageCoords[0]-800, y=imageCoords[1], clicks=1, button='right', duration=.1)
            time.sleep(.2)
            pyautogui.mouseUp(button='right')
            time.sleep(.8)
            keyHelper.PressKey(0x1E)
            time.sleep(.2)
            pyautogui.moveTo(imageCoords[0]+10, imageCoords[1]-10, duration=1)
            pyautogui.click(imageCoords[0]+10, imageCoords[1]-10, clicks=1, button='left', duration=.1)
            time.sleep(.2)
            pyautogui.mouseUp(button='left')
            time.sleep(.2)
            keyHelper.ReleaseKey(0x1E)

        if curr % 15 == 2:
            print("pressing CTRL Q")
            #upgrade Q
            keyHelper.PressKey(0x1D)  # CTRL
            keyHelper.PressKey(0x10)  # Q
            time.sleep(.1)
            keyHelper.ReleaseKey(0x1D)
            keyHelper.ReleaseKey(0x10)

        curr+=1

        if curr % 15 ==0:
            #close the menu if it some how is still open
            closeOptions()

            #check for end of game
            if openCVLocate.locateCenter(imgpath + '/continue.PNG') is not None:
                pyautogui.click(openCVLocate.locateCenter(imgpath + '/continue.PNG'), duration=.6)
                break

        time.sleep(2)

def closeOptions():
    if(openCVLocate.locateCenter(imgpath + '/options.PNG') != None):
        keyHelper.PandRKey(0x01)

if __name__ == "__main__":
    rundownmid("blue")