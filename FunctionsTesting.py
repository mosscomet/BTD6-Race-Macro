import time
import pyautogui
import pydirectinput
import random

# Configuration
originalScreenWidth = 2560
originalScreenHeight = 1440
screenWidth, screenHeight = pyautogui.size()

widthRatio = screenWidth / originalScreenWidth
heightRatio = screenHeight / originalScreenHeight

UseDefaultKeybinds = True

# Data
monkeys = {
    "dart": {"key":"q", "count":0},
    "boomerang": {"key":"w", "count":0},
    "bomb": {"key":"e", "count":0},
    "tack": {"key":"r", "count":0},
    "ice": {"key":"t", "count":0},
    "glue": {"key":"y", "count":0},
    "desperado": {"key":None, "count":0},
    "sniper": {"key":"z", "count":0}, 
    "sub": {"key":"x", "count":0},
    "boat": {"key":"c", "count":0},
    "plane": {"key":"v", "count":0},
    "heli": {"key":"b", "count":0},
    "mortar": {"key":"n", "count":0},
    "dartling": {"key":"m", "count":0},
    "wizard": {"key":"a", "count":0},
    "super": {"key":"s", "count":0},
    "ninja": {"key":"d", "count":0},
    "alch": {"key":"f", "count":0},
    "druid": {"key":"g", "count":0},
    "mermonkey": {"key":None, "count":0},
    "farm": {"key":"h", "count":0},
    "spike": {"key":"j", "count":0},
    "village": {"key":"k", "count":0},
    "engi": {"key":"l", "count":0},
    "beast": {"key":"i", "count":0},
    "hero": {"key":"u", "count":0}
}

# Stores placed monkeys as a dictionary entry: {"id": "dart1", "x":100, "y":200, "target":first, "upgrades":000}
PlacedMonkeys = []


# Helper Functions
def scale_coords(x,y):
    return int(x*widthRatio), int(y*heightRatio)

def SelectMonkey(MonkeyName: str):
    MonkeyName = MonkeyName.lower()
    if MonkeyName in monkeys and monkeys[MonkeyName]["key"]:
        pydirectinput.press(monkeys[MonkeyName]["key"])
    else:
        print("No keybind for {MonkeyName}")


# Monkey based functions
def PlaceMonkey(x, y, MonkeyName: str):
    MonkeyName = MonkeyName.lower()
    SelectMonkey(MonkeyName)

    sx, sy = scale_coords(x, y)
    if MonkeyName in monkeys:
        pydirectinput.moveTo(x, y, 0.1)
        pydirectinput.leftClick()
        monkeys[MonkeyName]["count"] += 1
        monkeyID = f"{MonkeyName}{monkeys[MonkeyName]['count']}"

        PlacedMonkeys.append({
            "id": monkeyID,
            "x": sx, 
            "y": sy, 
            "target": "first",
            "upgrades": "000"
        })
        print(f"Placed {monkeyID}")

def UpgradeMonkey(monkeyID: str, UpgradePath: str): 
    targetMonkey = None
    for m in PlacedMonkeys:
        if m["id"] == monkeyID:
            targetMonkey = m
            break
    if targetMonkey == None:
        print(f"Cant find {monkeyID}")
        return
    
    pyautogui.moveTo(targetMonkey["x"],targetMonkey["y"])
    pydirectinput.leftClick()
    
    time.sleep(0.1)

    currentUpgrades = []
    for digit in targetMonkey["upgrades"]:
        currentUpgrades.append(int(digit))
    
    print(currentUpgrades)
    time.sleep(0.1)
    
    targetUpgrades = []
    for digit in UpgradePath:
        targetUpgrades.append(int(digit))
    
    print(targetUpgrades)
    time.sleep(0.1)

    pressesNeeded = []
    for i in range(3):
        diff = targetUpgrades[i]-currentUpgrades[i]
        if diff < 0:
            diff = 0
        pressesNeeded.append(diff)
    
    print(pressesNeeded)
    time.sleep(0.1)

    keys = [",",".","/"]
    for i in range(3):
        for j in range(pressesNeeded[i]):
            pydirectinput.press(keys[i])
            time.sleep(0.01)
    
    targetMonkey["upgrades"] = UpgradePath
    time.sleep(0.1)
    pydirectinput.press("esc")


# Menu Functions
def Pause():
    pydirectinput.press("esc")

def GoHome():
    Pause()
    time.sleep(0.1)
    pyautogui.moveTo(int(1130*widthRatio),int(1130*heightRatio))
    pydirectinput.leftClick()

def Restart():
    Pause()
    time.sleep(0.1)
    pyautogui.moveTo(int(1430*widthRatio),int(1130*heightRatio))
    pydirectinput.leftClick()
    time.sleep(0.1)
    pyautogui.moveTo(int(1510*widthRatio),int(970*heightRatio))
    pydirectinput.leftClick()





time.sleep(3)

PlaceMonkey(800,800,"dart")

print(PlacedMonkeys)

time.sleep(2)

UpgradeMonkey("dart1","220")

PlaceMonkey(800,1200,"dart")

time.sleep(2)

UpgradeMonkey("dart1","250")

print(PlacedMonkeys)
