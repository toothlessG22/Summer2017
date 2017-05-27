import time
import pyautogui

if __name__ == "__main__":
    import keyHelper, openCVLocate
    imgpath = "../img"
else:
    from lib import keyHelper, openCVLocate
    imgpath = "img"

def rowdownmid(team):
    # assume loaded
    # click in screen
    imageCoords = None
    if (team == "blue"):
        while imageCoords is None:
            imageCoords = openCVLocate.locateCenter(imgpath + '/blueTeam.PNG')
    else:
        imageCoords = None
    clickInGame(imageCoords)
    # press y to lock camera
    keyHelper.PandRKey(keyHelper.cToHex('y'))
    # buy dorans blade

    # main loop
    while True:

        time.sleep(1)

def clickInGame(imageCoords):
    pyautogui.moveTo(imageCoords, duration=2)
    pyautogui.click(imageCoords, duration=.1)

def back():
    keyHelper.PandRKey(keyHelper.cToHex('b'))
    time.sleep(8.5)
