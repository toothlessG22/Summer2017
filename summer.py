import sys
import time

from lib import autoAccept, autoQueue, checkLoad, lockIn, runItDownMid, clickX

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
