import time

from PIL import ImageGrab

from lib import openCVLocate

start = time.time()
print(openCVLocate.locateCenter('img/play.PNG'))
im = ImageGrab.grab()
print(time.time() - start)
im.save('t.png')