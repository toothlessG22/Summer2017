from PIL import ImageGrab
import numpy as np
from lib import openCVLocate
from lib import OCR
import math
import time

im = np.array(ImageGrab.grab().convert('RGB'))
BTcoords = openCVLocate.locateCenter('img/blueTeam.png')

while True:
    im = np.array(ImageGrab.grab().convert('RGB'))
    ctime = time.clock()
    print("H: " + OCR.getWhiteText(im, math.floor(BTcoords[0] - 545), 26, math.floor(BTcoords[1] + 120), 12, lower=150)) # Health
    print(time.clock() - ctime)

    time.sleep(max(2-(time.clock()-ctime), 0))