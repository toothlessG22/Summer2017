import openCVLocate
import time

start = time.time()
print(openCVLocate.locateCenter('img/play.PNG'))
print(time.time() - start)