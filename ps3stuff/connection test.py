import pygame
from time import sleep

discon = False 
def check_pad():
    global discon
    pygame.joystick.quit()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    if not joystick_count:
        if not discon:
            print "reconnect please"
            discon = True
        sleep(1)
        check_pad()
    else:
        print "connected"
        discon = False

while True:
    check_pad()
