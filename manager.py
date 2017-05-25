from lib import openCVLocate, keyHelper
import sys
import time
import pyautogui

def checkForLogin(user, pw):
    # click sign in button to reset mouse cursor
    if(openCVLocate.locateCenter('img/signIn.png') == None):
        return
    pyautogui.click(openCVLocate.locateCenter('img/signIn.png'))
    time.sleep(1)
    keyHelper.PandRKey(0x0F) # tab
    keyHelper.sendString(user)
    keyHelper.PandRKey(0x0F)  # tab
    keyHelper.sendString(pw)
    keyHelper.PandRKey(keyHelper.cToHex('enter'))

if __name__ == "__main__":
    if(sys.argv.__len__() < 3):
        print('needs more params')
    else:
        while True:
            checkForLogin(sys.argv[1], sys.argv[2])
            time.sleep(60)