import cv2
import numpy as np
from PIL import ImageGrab

def locateCenter(imgfile, thold=.8):
    img_rgb = np.array(ImageGrab.grab().convert('RGB'))
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(imgfile, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = thold
    locs = []
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        locs.append((pt[0] + w/2, pt[1] + h/2))

    if(locs.__len__() == 0):
        return None
    else:
        return locs[0]