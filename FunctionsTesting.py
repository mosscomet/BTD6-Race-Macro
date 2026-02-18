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
# desperado and mermonkey do not have default keybinds, left blank

NumberMonkeysPlaced = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

PlacedMonkeys = []

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
    
    for i in range (len(MonkeyNames)):
          if(MonkeyNames[i] == MonkeyName.lower()):
              NumberMonkeysPlaced[i] += 1
              break
    
    PlacedMonkeys.append([MonkeyName + str(NumberMonkeysPlaced[i]),xCoord,yCoord]) 

def UpgradeUnderCursor(UpgradePath: str):
    pydirectinput.leftClick()
    UpgradePresses = list(UpgradePath)
    print(UpgradePresses)
    time.sleep(0.01)
    for i in range(3):
        for j in range(int(UpgradePresses[i])):
            if i == 0:
                pydirectinput.press(",")
                print(",")
            if i == 1:
                pydirectinput.press(".")
                print(".")
            if i == 2:
                pydirectinput.press("/")
                print("/")
    pydirectinput.press("esc") # close upgrade menu

def UpgradeMonkey(SpecificMonkeyName: str, UpgradePath: str):
  # Should use stored monkey names to return to a monkey at a certain coordinate, upgrade it based on a certain amount
  for i in range(len(PlacedMonkeys)):
    if PlacedMonkeys[i][0] == SpecificMonkeyName:
      pyautogui.moveTo(PlacedMonkeys[i][1],PlacedMonkeys[i][2])
      UpgradeUnderCursor(UpgradePath)
  return


PlaceMonkey(400,800,"tack")

PlaceMonkey(1000,1300,"plane")
UpgradeUnderCursor("203")

PlaceMonkey(1250,1300,"plane")
UpgradeUnderCursor("203")

PlaceMonkey(1450,1350,"hero")

print(PlacedMonkeys)

time.sleep(3)
UpgradeMonkey("plane1","100")
UpgradeMonkey("plane2","002")
UpgradeMonkey("tack1","502")
