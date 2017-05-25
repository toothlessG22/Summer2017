import runItDownMid
import autoQueue
import autoAccept
import checkLoad
import clickX
import lockIn
import sys
import time

if __name__ == "__main__":
    while True:
        autoQueue.autoQueue(sys.argv[1])
        autoAccept.autoAccept()
        lockIn.lockIn(['ashe', 'jhin', 'vayne'])
        # wait for game to load
        checkLoad.waitForLoad()
        team = checkLoad.checkTeam()

        if(sys.argv[2] == "runitdownmid"):
            runItDownMid.rundownmid(team)
        else:
            runItDownMid.rundownmid(team)

        clickX.clickX()
        time.sleep(3)
