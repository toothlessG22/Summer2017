import sys
import time
import pyautogui

if __name__ == "__main)":
    import openCVLocate
    imgpath = "../img"
else:
    from lib import openCVLocate
    imgpath = "img"

def autoQueue(queue):
    if queue == "intro":
        Qimage = "../img/introQueue.PNG"
    elif queue == "beginner":
        Qimage = "../img/beginnerQueue.PNG"
    elif queue == "intermediate":
        Qimage = "../img/intermediateQueue.PNG"
    else:
        Qimage = "../img/introQueue.PNG"

    #wait for play
    while openCVLocate.locateCenter(imgpath + '/play.PNG') == None:
        print("waiting for play")
        time.sleep(2)
    pyautogui.click(openCVLocate.locateCenter(imgpath + '/play.PNG'), duration=.06)
    pyautogui.click(openCVLocate.locateCenter(imgpath + '/play.PNG'), duration=.06)
    print("play clicked")
    #wait for coop v ai
    CvAIcount = 0
    while openCVLocate.locateCenter(imgpath + '/CoopVAI.PNG') == None:
        print("waiting for coop")
        time.sleep(2)
        CvAIcount += 1
        if(CvAIcount > 5):
            break
    pyautogui.click(openCVLocate.locateCenter(imgpath + '/CoopVAI.PNG'), duration=.07)
    print("CoopVAI clicked")

    #wait for queue
    Qcount = 0
    while openCVLocate.locateCenter(Qimage) == None:
        print("waiting for Q")
        time.sleep(2)
        Qcount += 1
        if (Qcount > 5):
            break
    pyautogui.click(openCVLocate.locateCenter(Qimage), duration=.07)
    print("Q clicked")

    #wait for confirm
    while openCVLocate.locateCenter(imgpath + '/confirmQueue.PNG') == None:
        print("waiting for confirm")
        time.sleep(2)
    pyautogui.click(openCVLocate.locateCenter(imgpath + '/confirmQueue.PNG'), duration=.07)
    print("ConfirmQ clicked")

    # wait for find match
    while openCVLocate.locateCenter(imgpath + '/findMatch.PNG') == None:
        print("waiting for find match")
        time.sleep(2)
    while openCVLocate.locateCenter(imgpath + '/findMatch.PNG') is not None:
        pyautogui.click(openCVLocate.locateCenter(imgpath + '/findMatch.PNG'), duration=.07)
    print("Find match clicked! Bye!")

if __name__ == "__main__":
    if(sys.argv.__len__() > 1):
        q = sys.argv[1]
    else:
        q = "intro"
    while True:
        autoQueue(q)

