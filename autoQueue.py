import pyautogui
import time
import sys
import openCVLocate

def autoQueue(queue):
    if queue == "intro":
        Qimage = "img/introQueue.PNG"
    elif queue == "beginner":
        Qimage = "img/beginnerQueue.PNG"
    elif queue == "intermediate":
        Qimage = "img/intermediateQueue.PNG"
    else:
        Qimage = "img/introQueue.PNG"

    #wait for play
    while openCVLocate.locateCenter('img/play.PNG') == None:
        print("waiting for play")
        time.sleep(2)
    pyautogui.click(openCVLocate.locateCenter('img/play.PNG'), duration=.06)

    #wait for coop v ai
    CvAIcount = 0
    while openCVLocate.locateCenter('img/CoopVAI.PNG') == None:
        print("waiting for coop")
        time.sleep(2)
        CvAIcount += 1
        if(CvAIcount > 5):
            break
    pyautogui.click(openCVLocate.locateCenter('img/CoopVAI.PNG'), duration=.07)

    #wait for queue
    Qcount = 0
    while openCVLocate.locateCenter(Qimage) == None:
        print("waiting for Q")
        time.sleep(2)
        Qcount += 1
        if (Qcount > 5):
            break
    pyautogui.click(openCVLocate.locateCenter(Qimage), duration=.07)

    #wait for confirm
    while openCVLocate.locateCenter('img/confirmQueue.PNG') == None:
        print("waiting for confirm")
        time.sleep(2)
    pyautogui.click(openCVLocate.locateCenter('img/confirmQueue.PNG'), duration=.07)

    # wait for find match
    while openCVLocate.locateCenter('img/findMatch.PNG') == None:
        print("waiting for find match")
        time.sleep(2)
    pyautogui.click(openCVLocate.locateCenter('img/findMatch.PNG'), duration=.07)

if __name__ == "__main__":
    if(sys.argv.__len__() > 1):
        q = sys.argv[1]
    else:
        q = "intro"
    while True:
        autoQueue(q)

