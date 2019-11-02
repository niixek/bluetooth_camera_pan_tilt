import pygame, sys
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)


# setup the pygame window
pygame.init()
window = pygame.display.set_mode((100, 100), 0, 32)

# how many joysticks connected to computer?
joystick_count = pygame.joystick.get_count()
print "There is " + str(joystick_count) + " joystick/s"

if joystick_count == 0:
    # if no joysticks, quit program safely
    print ("Error, I did not find any joysticks")
    pygame.quit()
    sys.exit()
else:
    # initialise joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

#axes = joystick.get_numaxes()
buttons = joystick.get_numbuttons()

#print "There is " + str(axes) + " axes"
print "There is " + str(buttons) + " button/s"

#def getAxis(number):
    #when nothing is  moved on an axis, the VALUE IS NOT EXACTLY ZERO
    #so this is used not "if joystick value not zero"
   # if joystick.get_axis(number) < -0.1 or joystick.get_axis(number) > 0.1:
      # value between 1.0 and -1.0
      # print "Axis value is %s" %(joystick.get_axis(number))
      # print "Axis ID is %s" %(number)
 
def getButton(number):
    # returns 1 or 0 - pressed or not
    while joystick.get_button(number) > 0:
    #if joystick.get_button(number):
      # just prints id of button
      print "Button ID is %s" %(number)
      #print "Relay 1 is on"
      #GPIO.output(11, GPIO.LOW)
   # print "Relay 1 is off"
    #GPIO.output(11, GPIO.HIGH)

while True:
    for event in pygame.event.get():
      # loop through events, if window shut down, quit program
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    #if axes != 0:
      #for i in range(axes):
       # getAxis(i)
    if buttons != 0:
      print buttons
      for i in range(buttons):
        getButton(i)
