from lib import openCVLocate, keyHelper
import sys
import time
import pyautogui


def checkForLogin(user, pw):
    time.sleep(3)
    # click sign in button to reset mouse cursort
    if(openCVLocate.locateCenter('img/signIn.png', thold=.9) == None):
        return
    pyautogui.click(openCVLocate.locateCenter('img/signIn.png'))
    #dbllcik on username field to highlight anything inthere
    userPos = openCVLocate.locateCenter('img/username.PNG')
    pyautogui.doubleClick(x=userPos[0], y=userPos[1]+15)
    time.sleep(1)
    keyHelper.sendString(user)
    # dbllcik on pw field to highlight anything inthere
    pwPos = openCVLocate.locateCenter('img/password.PNG')
    pyautogui.doubleClick(x=pwPos[0], y=pwPos[1] + 15)
    keyHelper.sendString(pw)
    keyHelper.PandRKey(keyHelper.cToHex('enter'))

if __name__ == "__main__":
    if(sys.argv.__len__() < 3):
        print('needs more params')
    else:
        while True:
            checkForLogin(sys.argv[1], sys.argv[2])
            time.sleep(60)