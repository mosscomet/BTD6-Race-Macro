# This macro is made to beat the Egg and Spoon race in 2:30 to 3:00
# April 7-10, 2023	
# Note, this does not work in fast forward mode

import time
import pyautogui
import random

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

def upgradeTopLeft():
    pyautogui.moveTo((screenWidth*0.1757),(screenHeight*0.4513),.25)
    pyautogui.click((screenWidth*0.1757),(screenHeight*0.4513))

def upgradeTopRight():
    pyautogui.moveTo((screenWidth*0.8085),(screenHeight*0.4513),.25)
    pyautogui.click((screenWidth*0.8085),(screenHeight*0.4513))

def upgradeLeftMiddle():
    pyautogui.moveTo((screenWidth*0.1757),(screenHeight*0.5902),.25)
    pyautogui.click((screenWidth*0.1757),(screenHeight*0.5902))

def upgradeRightMiddle():
    pyautogui.moveTo((screenWidth*0.8085),(screenHeight*0.5902),.25)
    pyautogui.click((screenWidth*0.8085),(screenHeight*0.5902))


time.sleep(5) #Pause to tab back in after running

for x in range(0, 3): #Change the higher number here to change how many times it loops
    #Open Race
    pyautogui.moveTo((screenWidth*0.96875),(screenHeight*0.5763),.5)
    pyautogui.click((screenWidth*0.96875),(screenHeight*0.5763))
    time.sleep(.2)

    #Click Race
    pyautogui.moveTo((screenWidth*0.45),(screenHeight*0.8),.5)
    pyautogui.click((screenWidth*0.45),(screenHeight*0.8))
    time.sleep(3)

    #Click Okay
    pyautogui.moveTo((screenWidth*0.5),(screenHeight*0.69444),.5)
    pyautogui.click((screenWidth*0.5),(screenHeight*0.69444))
    time.sleep(.75)

    #Place hero
    pyautogui.moveTo((screenWidth*0.8925),(screenHeight*0.2187),.5)
    pyautogui.click((screenWidth*0.8925),(screenHeight*0.2187))
    pyautogui.moveTo((screenWidth*0.1152),(screenHeight*0.7361),.5)
    pyautogui.click((screenWidth*0.1152),(screenHeight*0.7361))
    time.sleep(0.1)
    pyautogui.click((screenWidth*0.1152),(screenHeight*0.7361))
    
    #Target Gwendolyn Cocktail Ability
    pyautogui.moveTo((screenWidth*0.8347),(screenHeight*0.2854),.5)
    pyautogui.click((screenWidth*0.8347),(screenHeight*0.2854))
    time.sleep(.75)
    pyautogui.moveTo((screenWidth*0.125),(screenHeight*0.7847),.5)
    pyautogui.click((screenWidth*0.125),(screenHeight*0.7847))
    time.sleep(.75)

    #Start Race
    pyautogui.moveTo((screenWidth*0.8958),(screenHeight*0.9351),.25)
    for x in range(0, 4):
        pyautogui.click((screenWidth*0.8958),(screenHeight*0.9351))
        time.sleep(0.1)

    #Send to round 21
    time.sleep(5.1)
    for x in range(4, 21):
        pyautogui.click((screenWidth*0.8958),(screenHeight*0.9351))
        time.sleep(0.1)

    #Hero Ability
    time.sleep(1)
    pyautogui.moveTo((screenWidth*0.102),(screenHeight*0.9537),.25)
    pyautogui.click((screenWidth*0.102),(screenHeight*0.9537))

    #Sell hero
    time.sleep(1.75)
    pyautogui.moveTo((screenWidth*0.8072),(screenHeight*0.8518),.25)
    pyautogui.click((screenWidth*0.8072),(screenHeight*0.8518))

    #Hero again
    pyautogui.moveTo((screenWidth*0.8925),(screenHeight*0.2187),.5)
    pyautogui.click((screenWidth*0.8925),(screenHeight*0.2187))
    pyautogui.moveTo((screenWidth*0.2968),(screenHeight*0.2330),.5)
    pyautogui.click((screenWidth*0.2968),(screenHeight*0.2330))
    time.sleep(3)

    # First Druid
    pyautogui.moveTo((screenWidth*0.9531),(screenHeight*0.55),0.25)
    for x in range(0,10):
        pyautogui.scroll(-1)
        time.sleep(.05)
    pyautogui.click((screenWidth*0.9531),(screenHeight*0.55))
    pyautogui.moveTo((screenWidth*0.3635),(screenHeight*0.2330),0.25)
    pyautogui.click((screenWidth*0.3635),(screenHeight*0.2330))

    #Send 31
    pyautogui.moveTo((screenWidth*0.8958),(screenHeight*0.9351),.25)
    for x in range(21, 31):
        pyautogui.click((screenWidth*0.8958),(screenHeight*0.9351))
        time.sleep(0.1)
    time.sleep(2)

    #Second Ability
    time.sleep(1)
    pyautogui.moveTo((screenWidth*0.102),(screenHeight*0.9537),.25)
    pyautogui.click((screenWidth*0.102),(screenHeight*0.9537))

    #Upgrade First Druid
    time.sleep(4)
    pyautogui.moveTo((screenWidth*0.3635),(screenHeight*0.2330),0.25)
    pyautogui.click((screenWidth*0.3635),(screenHeight*0.2330))
    upgradeTopRight()
    upgradeRightMiddle()
    upgradeRightMiddle()
    upgradeRightMiddle()
    time.sleep(1)
    upgradeTopRight()
    pyautogui.moveTo((screenWidth*0.3635),(screenHeight*0.2330),0.25)
    pyautogui.click((screenWidth*0.3635),(screenHeight*0.2330))
    
    #Send 39
    pyautogui.moveTo((screenWidth*0.8958),(screenHeight*0.9351),.25)
    for x in range(31, 39):
        pyautogui.click((screenWidth*0.8958),(screenHeight*0.9351))
        time.sleep(0.1)
    time.sleep(0.5)

    # Second Druid
    pyautogui.moveTo((screenWidth*0.9531),(screenHeight*0.55),0.25)
    for x in range(0,10):
        pyautogui.scroll(-1)
        time.sleep(.05)
    pyautogui.click((screenWidth*0.9531),(screenHeight*0.55))
    pyautogui.moveTo((screenWidth*0.4812),(screenHeight*0.4326),0.25)
    pyautogui.click((screenWidth*0.4812),(screenHeight*0.4326))
    time.sleep(.1)
    pyautogui.click((screenWidth*0.4812),(screenHeight*0.4326))
    upgradeTopLeft()
    upgradeTopLeft()
    upgradeLeftMiddle()
    upgradeLeftMiddle()
    time.sleep(1)
    upgradeLeftMiddle()
    pyautogui.click((screenWidth*0.4812),(screenHeight*0.4326))

    #Sub
    pyautogui.moveTo((screenWidth*0.9531),(screenHeight*0.4513),0.25)
    for x in range(0,10):
        pyautogui.scroll(1)
        time.sleep(.05)
    pyautogui.click((screenWidth*0.9531),(screenHeight*0.4513))
    pyautogui.moveTo((screenWidth*0.3710),(screenHeight*0.7361),0.25)
    pyautogui.click((screenWidth*0.3710),(screenHeight*0.7361))
    time.sleep(.1)
    pyautogui.click((screenWidth*0.3710),(screenHeight*0.7361))
    time.sleep(1)
    upgradeTopRight()
    upgradeTopRight()
    upgradeTopRight()
    time.sleep(4.5)
    upgradeTopRight()
    upgradeRightMiddle()
    upgradeRightMiddle()
    pyautogui.click((screenWidth*0.3710),(screenHeight*0.7361))

    #Send 49
    pyautogui.moveTo((screenWidth*0.8958),(screenHeight*0.9351),.25)
    for x in range(21, 31):
        pyautogui.click((screenWidth*0.8958),(screenHeight*0.9351))
        time.sleep(0.1)
    time.sleep(12)

    # Upgrade Second Druid
    pyautogui.moveTo((screenWidth*0.4812),(screenHeight*0.4326),0.25)
    pyautogui.click((screenWidth*0.4812),(screenHeight*0.4326))
    upgradeLeftMiddle()
    pyautogui.moveTo((screenWidth*0.4812),(screenHeight*0.4326),0.25)
    pyautogui.click((screenWidth*0.4812),(screenHeight*0.4326))
    time.sleep(3)

    # Third Druid
    pyautogui.moveTo((screenWidth*0.9531),(screenHeight*0.55),0.25)
    for x in range(0,10):
        pyautogui.scroll(-1)
        time.sleep(.05)
    pyautogui.click((screenWidth*0.9531),(screenHeight*0.55))
    pyautogui.moveTo((screenWidth*0.5156),(screenHeight*0.3826),0.25)
    pyautogui.click((screenWidth*0.5156),(screenHeight*0.3826))
    time.sleep(.1)
    pyautogui.click((screenWidth*0.5156),(screenHeight*0.3826))
    time.sleep(9)
        #Change all of the words here from Right to Left to make the game go faster, leaving them at Right will result in the 3rd druid being unupgraded
    upgradeTopLeft()
    upgradeLeftMiddle()
    upgradeLeftMiddle()
    upgradeLeftMiddle()
    upgradeLeftMiddle()

    pyautogui.click((screenWidth*0.5156),(screenHeight*0.3826))


    #Send 65
    pyautogui.moveTo((screenWidth*0.8958),(screenHeight*0.9351),.25)
    for x in range(49, 65):
        pyautogui.click((screenWidth*0.8958),(screenHeight*0.9351))
        time.sleep(0.1)

    # Dart
    time.sleep(3)
    pyautogui.moveTo((screenWidth*0.9531),(screenHeight*0.2592),0.25)
    for x in range(0,10):
        pyautogui.scroll(1)
        time.sleep(.05)
    pyautogui.click((screenWidth*0.9531),(screenHeight*0.2592))
    pyautogui.moveTo((screenWidth*0.2695),(screenHeight*0.4236),0.25)
    pyautogui.click((screenWidth*0.2695),(screenHeight*0.4236))
    time.sleep(.1)
    pyautogui.click((screenWidth*0.2695),(screenHeight*0.4236))
    upgradeTopRight()
    upgradeTopRight()
    upgradeTopRight()
    upgradeTopRight()
    upgradeRightMiddle()
    upgradeRightMiddle()
    pyautogui.click((screenWidth*0.2695),(screenHeight*0.4236))

    #Full Send
    pyautogui.moveTo((screenWidth*0.8958),(screenHeight*0.9351),.25)
    for x in range(65, 73):
        pyautogui.click((screenWidth*0.8958),(screenHeight*0.9351))
        time.sleep(0.1)
    time.sleep(10)

    # Upgrade Dart
    pyautogui.moveTo((screenWidth*0.2695),(screenHeight*0.4236),0.25)
    pyautogui.click((screenWidth*0.2695),(screenHeight*0.4236))
    upgradeTopRight()
    time.sleep(random.randint(0,10))

    #Place glue
    pyautogui.moveTo((screenWidth*0.9531),(screenHeight*0.3395),0.25)
    for x in range(0,10):
        pyautogui.scroll(1)
        time.sleep(.05)
    pyautogui.click((screenWidth*0.9531),(screenHeight*0.3395))
    pyautogui.moveTo((screenWidth*0.1523),(screenHeight*0.3611),0.4)
    pyautogui.click((screenWidth*0.1523),(screenHeight*0.3611))
    pyautogui.click((screenWidth*0.1523),(screenHeight*0.3611))
    upgradeTopRight()
    upgradeTopRight()
    upgradeTopRight()
    upgradeTopRight()
    time.sleep(random.randint(25,40))


    #Upgrade glue to 5-2-0
    upgradeTopRight()
    upgradeRightMiddle()
    upgradeRightMiddle()

    #Wait for race to end
    time.sleep(20)
    pyautogui.moveTo((screenWidth*0.4335),(screenHeight*0.7708),.25)
    pyautogui.click((screenWidth*0.4335),(screenHeight*0.7708))
    time.sleep(5)
