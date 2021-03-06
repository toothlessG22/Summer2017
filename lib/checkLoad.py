import time

if __name__ == "__main)":
    import openCVLocate
    imgpath = "../img"
else:
    from lib import openCVLocate
    imgpath = "img"


def waitForLoad():
    while(openCVLocate.locateCenter(imgpath + '/blueTeam.png')) == None:
        print("waiting for load")
        if(openCVLocate.locateCenter(imgpath + '/dodge.PNG')) is not None:
            return False
        time.sleep(5)
    print("loaded")
    return True

def checkTeam():
    if(openCVLocate.locateCenter(imgpath + '/blueTeam.png')):
        return 'blue'
    else:
        return 'red'