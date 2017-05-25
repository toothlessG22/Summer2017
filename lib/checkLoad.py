import time

from lib import openCVLocate


def waitForLoad():
    while(openCVLocate.locateCenter('img/blueTeam.png')) == None:
        print("waiting for load")
        time.sleep(5)
    return

def checkTeam():
    if(openCVLocate.locateCenter('img/blueTeam.png')):
        return 'blue'
    else:
        return 'red'