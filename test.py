from PIL import ImageGrab
import numpy as np
from lib import openCVLocate
from PIL import Image
from lib import OCR
import math
import cv2
import time

c = 0

t = time.clock()
BTcoords = openCVLocate.locateCenter('img/blueTeamTT.png')
print("BT:" + str(time.clock() - t))
botimg = cv2.imread('img/Bot.png' ,0)

while True:
    ctime = time.clock()
    t = time.clock()
    im = ImageGrab.grab()
    print("IG:" + str(time.clock() - t))
    t = time.clock()
    im = im.convert('RGB')
    print("CON:" + str(time.clock() - t))
    t = time.clock()
    im = np.array(im)
    print("NP:" + str(time.clock() - t))
    t = time.clock()
    y = math.floor(BTcoords[1]) + 67
    x = math.floor(BTcoords[0]) - 672
    c_img_array = im[y:y+2, x:x+293]
    for i in range(292, 0, -1):
        if(int(c_img_array[0][i][0]) * int(c_img_array[0][i][1]) * int(c_img_array[0][i][2]) > 1000000):
            print(i/293)
            break
    print("H:" + str(time.clock() - t))
    t = time.clock()
    print(openCVLocate.locateCenter(botimg, img_rgb=im[math.floor(BTcoords[1] - 700): math.floor(BTcoords[1] + 85), math.floor(BTcoords[0] - 1000): math.floor(BTcoords[0] + 40)],
                                    isFile=False))
    print("LB:" + str(time.clock() - t))
    time.sleep(max(1 - (time.clock() - ctime ), 0))

Image.fromarray(im).save('t1.png')
Image.fromarray(c_img_array).save('t2.png')