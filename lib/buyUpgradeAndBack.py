import math
import time
try:
    from lib import keyHelper, OCR
except ImportError:
    import keyHelper, OCR

def buy(buyorder, screenshot, BTcoords, xoff=-290, yoff=133):
    text = OCR.getWhiteText(screenshot, math.floor(BTcoords[0] + xoff), 40, math.floor(BTcoords[1] + yoff), 15, lower=120)
    if text is '':
        gold = 0
    else:
        gold = int(text)
    while gold >= buyorder[buyorder[0]][1] and buyorder[0] < buyorder.__len__():
        print("buying " + str(buyorder[buyorder[0]][0]))
        keyHelper.PandRKey(0x19)
        time.sleep(1)
        keyHelper.PressKey(0x1D)  # CTRL
        time.sleep(1)
        keyHelper.PandRKey(0x1C)  # RTRN
        time.sleep(1)
        keyHelper.ReleaseKey(0x1D)  # CTRL
        keyHelper.sendString(buyorder[buyorder[0]][0])
        keyHelper.PandRKey(0x1C)  # RTRN
        keyHelper.PandRKey(0x1C)  # RTRN
        keyHelper.PandRKey(0x01)  # ESC
        gold -= buyorder[buyorder[0]][1]
        buyorder[0] += 1
        time.sleep(2)

def upgrade(upgradeorder):
    print("upgrading " + upgradeorder[upgradeorder[0]])
    keyHelper.PressKey(0x1D)  # CTRL
    time.sleep(1)
    keyHelper.PandRKey(keyHelper.cToHex(upgradeorder[upgradeorder[0]]))
    time.sleep(1)
    keyHelper.ReleaseKey(0x1D)  # CTRL
    upgradeorder[0] += 1

def back():
    print("backing...")
    keyHelper.PandRKey(keyHelper.cToHex('b'))
    time.sleep(16)