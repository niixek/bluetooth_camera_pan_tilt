'''
Created by Kexin Chen, CIM 2018
Orchard Park High School
I used "Pygame" to create the graphical stuff.
As a side note: The program lags ocassionally, and it may be due the
Raspberry Pi itself. Not 100% sure
'''
#A bunch of imports and Raspberry Pi pin setup stuff
import pygame, sys
from time import sleep
import RPi.GPIO as GPIO
import os
from multiprocessing import Process
from threading import Thread
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

#Intializes the window and the controller
pygame.init()
window = pygame.display.set_mode((700,400))
pygame.display.set_caption('Pan-Tilt Controller Visual')
joystick_count = pygame.joystick.get_count()
joystick = pygame.joystick.Joystick(0)
joystick.init()

#Some color variable stuff, based on (R,G,B)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

#Position variables for the location of pictures
p = 175
q = 175
x = (700 * .45)
y = (400 * .85)

#Speed variables, we didn't use these
currentSpeed = 2
whatSpeed = ""

'''
A lot of probably unnecessary code, but imports the pictures into
the program and scales them down to whatever size you want them to be.
If you want the program to have pictures on boot, you MUST specify exact
location of file. If you're only using it temporarily, you must put
the picture in the same location as the python script.
'''
startButton = pygame.image.load('/home/pi/Desktop/start button.png')
startButton = pygame.transform.scale(startButton, (50,50))
qtv = pygame.image.load('/home/pi/Desktop/Capture.PNG')
qtv = pygame.transform.scale(qtv, (150, 150))
default = pygame.image.load('/home/pi/Desktop/dpad.png').convert_alpha()
default = pygame.transform.scale(default, (p,q))
up = pygame.image.load('/home/pi/Desktop/d-pad up.png').convert_alpha()
up = pygame.transform.scale(up, (p,q))
down = pygame.image.load('/home/pi/Desktop/d-pad down.png').convert_alpha()
down = pygame.transform.scale(down, (p,q))
left = pygame.image.load('/home/pi/Desktop/left.png').convert_alpha()
left = pygame.transform.scale(left, (p,q))
right = pygame.image.load('/home/pi/Desktop/d-pad right.png').convert_alpha()
right = pygame.transform.scale(right, (p,q))
upleft = pygame.image.load('/home/pi/Desktop/d-pad up-left.png').convert_alpha()
upleft = pygame.transform.scale(upleft, (p,q))
upright = pygame.image.load('/home/pi/Desktop/d-pad up-right.png').convert_alpha()
upright = pygame.transform.scale(upright, (p,q))
downleft = pygame.image.load('/home/pi/Desktop/d-pad down-left.png').convert_alpha()
downleft = pygame.transform.scale(downleft, (p,q))
downright = pygame.image.load('/home/pi/Desktop/d-pad down-right.png').convert_alpha()
downright = pygame.transform.scale(downright, (p,q))

#Circles that represented speeds, we didn't use these.
'''slowest = pygame.draw.circle(window, red, (90,90), 30)
slow = pygame.draw.circle(window, red, (160,90), 30)
normal = pygame.draw.circle(window, green, (230,90), 30)
fast = pygame.draw.circle(window, red, (300,90), 30)
fastest = pygame.draw.circle(window, red, (370,90), 30)
'''

'''
Here are the fonts I used, if you want to know what other fonts are
available: open up the python console, type import pygame, then type
"pygame.font.get_fonts()"
'''
font = pygame.font.SysFont(None, 25)
largeText = pygame.font.SysFont('robotocondensed', 60)
buttonText = pygame.font.SysFont('droidnaskhshiftalt', 50)
credText = pygame.font.SysFont('dejavuserif', 30)
credText2 = pygame.font.SysFont('freemono', 24)
credText3 = pygame.font.SysFont('droidserif', 20)
credText4 = pygame.font.SysFont('freemono', 18)

'''
This asks for which direction is being pressed and displays
the appropriate picture
'''
def whichDir(picture):
    window.blit(picture, (700*.7, 400*.3))
    pygame.display.update()

#Creates essentially a textbox
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

'''
Here's all of our text located in the GUI:
exitMessage is the instructions to quit program
guiMsg is the text at the top
credits are the credits :^)
groups are the groups :^>
names are our names :^O
creditDisplay is written so I could switch between the groups/names
'''
def exitMessage():
    global largeText
    TextSurf, TextRect = text_objects("Press     to exit.", largeText)
    TextRect.center = (700 * .51, 400 * .9)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def guiMsg():
    global buttonText
    TextSurf, TextRect = text_objects('Pan-Tilt Camera Head GUI', buttonText)
    TextRect.center = (700 * .51, 400 * .1)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def credit():
    global credText
    TextSurf, TextRect = text_objects("Created by Mr. Kennedy's CIM 2018", credText)
    TextRect.center = (700 * .51, 400 * .25)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def group1():
    global credText2
    TextSurf, TextRect = text_objects('Programmers:', credText2)
    TextRect.center = (700 * .51, 400 * .35)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def group2():
    global credText2
    TextSurf, TextRect = text_objects('Engineers:', credText2)
    TextRect.center = (700 * .51, 400 * .35)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def group3():
    global credText2
    TextSurf, TextRect = text_objects('CAD Wizards:', credText2)
    TextRect.center = (700 * .51, 400 * .35)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def group4():
    global credText2
    TextSurf, TextRect = text_objects('Engineer and Candy Man:', credText4)
    TextRect.center = (700 * .51, 400 * .35)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def names1(name):
    global credText3
    TextSurf, TextRect = text_objects(name, credText3)
    TextRect.center = (700 * .51, 400 * .45)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def names2(name):
    global credText3
    TextSurf, TextRect = text_objects(name, credText3)
    TextRect.center = (700 * .51, 400 * .53)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def names3(name):
    global credText3
    TextSurf, TextRect = text_objects(name, credText3)
    TextRect.center = (700 * .51, 400 * .61)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def names4(name):
    global credText3
    TextSurf, TextRect = text_objects(name, credText3)
    TextRect.center = (700 * .51, 400 * .69)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def names5(name):
    global credText3
    TextSurf, TextRect = text_objects(name, credText3)
    TextRect.center = (700 * .51, 400 * .77)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def names6(name):
    global credText3
    TextSurf, TextRect = text_objects(name, credText3)
    TextRect.center = (700 * .51, 400 * .77)
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    
def creditDisplay(which):
    if which == 1:
        group1()
        names1('Kexin Chen')
        names2('Ben Stuhr')
    elif which == 2:
        group2()
        names1('Will Barsottelli')
        names2('Simon Bond')
        names3('Ben King')
        names4('Jack Watson')
    elif which == 3:
        group3()
        names1('Kelsey Janaski')
        names2('Cletus Tepas')
    elif which == 4:
        group4()
        names1('David Cappello')

'''
Here's the code that turns the relays on.
I probably could've optimized the code, but it was easier at the time
to split up the code by Relays. The sleep is most likely necessary so
the Relays have time to check what state they are in. Not 100% sure.
'''
def turnOnR1():
    GPIO.output(12, GPIO.LOW)
    #print "LEFT"
    sleep(.1)

def turnOnR2():
    GPIO.output(11, GPIO.LOW)
    #print "RIGHT"
    sleep(.1)

def turnOnR3():
    GPIO.output(15, GPIO.LOW)
    #print "UP"
    sleep(.1)

def turnOnR4():
    GPIO.output(16, GPIO.LOW)
   # print "DOWN"
    sleep(.1)

#Resets the direction to the default picture
def dirErase():
    window.blit(default, (700*.7, 400*.3))
    pygame.display.update()

#Resets all relays to the OFF state
def turnOff():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    sleep(.1)

def creditErase():
    pygame.draw.rect(window, black, (700*.33, 400*.3, 260, 210))
    pygame.display.update()

'''
Here is where I displayed all of the initial default pictures and text.
They do not go in the while loop because they only need to be shown once.
'''
window.blit(startButton, (x,y))
window.blit(qtv, (700*.1, 400*.35))
window.blit(default, (700*.7, 400*.3))

exitMessage()
guiMsg()
credit()


'''
The purpose of this while loop is that it goes through all of this code
all the time while the code is running and updates as necessary.
'''
def loop1():
    while True:
        #You need this to check for controller events (button pushes)
        events = pygame.event.get()
        for event in events:
            #This does the below code if the button is held down
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(7):
                    if joystick.get_button(4):
                        turnOnR3()
                        turnOnR1()
                        whichDir(upleft)
                    elif joystick.get_button(6):
                        turnOnR4()
                        turnOnR1()
                        whichDir(downleft)
                    else:
                        turnOnR1()
                        whichDir(left)
                elif joystick.get_button(5):
                    if joystick.get_button(4):
                        turnOnR3()
                        turnOnR2()
                        whichDir(upright)
                    elif joystick.get_button(6):
                        turnOnR4()
                        turnOnR2()
                        whichDir(downright)
                    else:
                        turnOnR2()
                        whichDir(right)
                elif joystick.get_button(4):
                    turnOnR3()
                    whichDir(up)
                elif joystick.get_button(6):
                    turnOnR4()
                    whichDir(down)
                elif joystick.get_button(3):
                    pygame.quit()
                    sys.exit()
            #Upon the button release, everything is reverted back to normal
            elif event.type == pygame.JOYBUTTONUP:
                turnOff()
                dirErase()

def loop2():
    while True:
        creditDisplay(1)
        sleep(5)
        creditErase()
        sleep(1)
        creditDisplay(2)
        sleep(5)
        creditErase()
        sleep(1)
        creditDisplay(3)
        sleep(5)
        creditErase()
        sleep(1)
        creditDisplay(4)
        sleep(5)
        creditErase()
        sleep(1)


Thread(target = loop1).start()
Thread(target = loop2).start()

'''
while True:
    #You need this to check for controller events (button pushes)
    events = pygame.event.get()
    for event in events:
        #This does the below code if the button is held down
        if event.type == pygame.JOYBUTTONDOWN:
            if joystick.get_button(7):
                if joystick.get_button(4):
                    turnOnR3()
                    turnOnR1()
                    whichDir(upleft)
                elif joystick.get_button(6):
                    turnOnR4()
                    turnOnR1()
                    whichDir(downleft)
                else:
                    turnOnR1()
                    whichDir(left)
            elif joystick.get_button(5):
                if joystick.get_button(4):
                    turnOnR3()
                    turnOnR2()
                    whichDir(upright)
                elif joystick.get_button(6):
                    turnOnR4()
                    turnOnR2()
                    whichDir(downright)
                else:
                    turnOnR2()
                    whichDir(right)
            elif joystick.get_button(4):
                turnOnR3()
                whichDir(up)
            elif joystick.get_button(6):
                turnOnR4()
                whichDir(down)
            elif joystick.get_button(3):
                pygame.quit()
                sys.exit()
        #Upon the button release, everything is reverted back to normal
        elif event.type == pygame.JOYBUTTONUP:
            turnOff()
            dirErase()
'''
'''
This is code to print the position of the joysticks. I couldn't get the up
and down motion of the joysticks to work... so it only prints out the left
and right positions, and zeroes for up and down.

        if event.type == pygame.JOYAXISMOTION:
            if joystick.get_axis(0) > .03 or joystick.get_axis(0) < -.03:
                leftJoy(1)
            elif joystick.get_axis(1) > .03 or joystick.get_axis(1) < -.03:
                leftJoy(2)
            elif joystick.get_axis(2) > .03 or joystick.get_axis(2) < -.03:
                rightJoy(1)
            elif joystick.get_axis(3) > .03 or joystick.get_axis(3) < -.03:
                rightJoy(2)
'''
'''
This is the graveyard of a bunch of code that we ended up not using either
because it complicated the program, we scrapped the idea, or it
lagged out the Pi way too much

def slowDown():
    global currentSpeed
    global whatSpeed
    currentSpeed -= 1
    if currentSpeed == 0:
        whatSpeed = "Slowest"
    elif currentSpeed == 1:
        whatSpeed = "Slow"
    elif currentSpeed == 2:
        whatSpeed = "Normal"
    elif currentSpeed == 3:
        whatSpeed = "Fast"
    elif currentSpeed == 4:
        whatSpeed = "Fastest"
    sleep(.2)

def speedUp():
    global currentSpeed
    currentSpeed += 1
    global whatSpeed
    if currentSpeed == 0:
        whatSpeed = "Slowest"
    elif currentSpeed == 1:
        whatSpeed = "Slow"
    elif currentSpeed == 2:
        whatSpeed = "Normal"
    elif currentSpeed == 3:
        whatSpeed = "Fast"
    elif currentSpeed == 4:
        whatSpeed = "Fastest"
    sleep(.2)

def colorChanger():
    pygame.draw.circle(window, red, (90,90), 30)
    pygame.draw.circle(window, red, (160,90), 30)
    pygame.draw.circle(window, red, (230,90), 30)
    pygame.draw.circle(window, red, (300,90), 30)
    pygame.draw.circle(window, red, (370,90), 30)

def speedState(num):
    global currentSpeed
    if currentSpeed == 0:
        pygame.draw.circle(window, green, (90,90), 30)
    elif currentSpeed == 1:
        pygame.draw.circle(window, green, (160,90), 30)
    elif currentSpeed == 2:
        pygame.draw.circle(window, green, (230,90), 30)
    elif currentSpeed == 3:
        pygame.draw.circle(window, green, (300,90), 30)
    elif currentSpeed == 4:
        pygame.draw.circle(window, green, (370,90), 30)

def speedText(text, pos1, pos2):
    global buttonText
    TextSurf, TextRect = text_objects(text, buttonText)
    TextRect.center = (700 * pos1, 400 * pos2)
    window.blit(TextSurf, TextRect)
    pygame.display.update

def leftJoy(num):
    if 1:
        print "L " + str(joystick.get_axis(0))
    elif 2:
        print "L " + str(joystick.get_axis(1))
        
def rightJoy(num):
    if 1:
        print "R " + str(joystick.get_axis(2))
    elif 2:
        print "R " + str(joystick.get_axis(3))
'''
           
