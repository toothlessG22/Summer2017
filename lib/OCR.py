import pytesseract
import numpy as np
import cv2
from PIL import Image
import time

def getWhiteText(img_array, x , width, y, height, lower=145, upper=256):
    c_img_array = img_array[y:y+height, x:x+width]
    res = cv2.resize(c_img_array, (3 * width, 3 * height), interpolation=cv2.INTER_CUBIC)

    low = np.array([lower, lower, lower], dtype="uint16")
    up = np.array([upper, upper, upper], dtype="uint16")
    mask = cv2.inRange(res, low, up)

    output = cv2.bitwise_and(res, res, mask=mask)

    img = Image.fromarray(output)
    img.save("t5.png")
    txt = pytesseract.image_to_string(img, config="digits")
    print(txt)
    return txt