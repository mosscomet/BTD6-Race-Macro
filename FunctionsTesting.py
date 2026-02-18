import time
import pyautogui
import pydirectinput
import random

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

time.sleep(2)

UseDefaultKeybinds = True # If set to true, will use default BTD6 keybinds for actions

MonkeyNames = ["dart","boomerang","bomb","tack","ice","glue", "desperado","sniper",
               "sub","boat","plane","heli","mortar","dartling","wizard","super",
               "ninja","alch","druid","mermonkey","farm","spike","village","engi","beast","hero"]

Keybinds = ["q","w","e","r","t","y","","z","x","c","v","b","n","m","a","s","d","f","g","","h","j","k","l","i","u"]



def SelectMonkey(MonkeyName: str):
    if UseDefaultKeybinds:
        keypress = ""
        for i in range (len(MonkeyNames)):
            if(MonkeyNames[i] == MonkeyName.lower()):
                keypress = Keybinds[i]
        print(keypress)
        print(MonkeyName)
        pydirectinput.press(keypress)
    else:
        pydirectinput.press(MonkeyName)
        return

def PlaceMonkey(xCoord,yCoord,MonkeyName: str):
    if MonkeyName != None:
        SelectMonkey(MonkeyName)
    pydirectinput.moveTo(xCoord,yCoord,0.1)
    pydirectinput.leftClick()

def UpgradeUnderCursor(UpgradePath: int):
    pydirectinput.leftClick()
    UpgradePresses = list(str(UpgradePath))
    print(UpgradePresses)
    time.sleep(0.01)
    for i in range(2):
        for j in range(int(UpgradePresses[i])):
            if i == 0:
                pydirectinput.press(",")
            if i == 1:
                pydirectinput.press(".")
            if i == 2:
                pydirectinput.press("/")


PlaceMonkey(1000,1000,"plane")
UpgradeUnderCursor(203)

