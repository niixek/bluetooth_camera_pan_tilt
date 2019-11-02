import pygame, sys
from time import sleep

pygame.init()
window = pygame.display.set_mode((700,400))
pygame.display.set_caption('Test')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (255,165,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
indigo = (111,0,255)
violet = (148,0,211)
x = 255
y = 255
z = 255

font = pygame.font.SysFont(None, 25)
largeText = pygame.font.SysFont('robotocondensed', 60)
buttonText = pygame.font.SysFont('dejavusans', 16)

startButton = pygame.image.load('start button.png')
startButton = pygame.transform.scale(startButton, (50,50))
slowest = pygame.draw.circle(window, red, (90,90), 30)
slow = pygame.draw.circle(window, red, (160,90), 30)
normal = pygame.draw.circle(window, green, (230,90), 30)
fast = pygame.draw.circle(window, red, (300,90), 30)
fastest = pygame.draw.circle(window, red, (370,90), 30)
#add this
dirStart = pygame.draw.rect(window, white, (700*.7, 400*.38, 150, 150))

def start():
    window.blit(startButton, (700*.45,400*.85))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def exitMessage(text):
    global largeText
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (700 * .51, 400 * .9)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def speedText(text, pos1, pos2):
    global buttonText
    TextSurf, TextRect = text_objects(text, buttonText)
    TextRect.center = (700 * pos1, 400 * pos2)
    window.blit(TextSurf, TextRect)
    pygame.display.update()

def colorChanger():
    pygame.draw.circle(window, red, (90,90), 30)
    pygame.draw.circle(window, red, (160,90), 30)
    pygame.draw.circle(window, red, (230,90), 30)
    pygame.draw.circle(window, red, (300,90), 30)
    pygame.draw.circle(window, red, (370,90), 30)

#add this
def whichDir(color):
    pygame.draw.rect(window, color, (700*.7, 400*.38, 150, 150))
    sleep(.2)

def colorCycle():
    pygame.draw.circle(window, red, (200,250), 50)
    sleep(.3)
    pygame.display.update()
    pygame.draw.circle(window, orange, (200,250), 50)
    sleep(.3)
    pygame.display.update()
    pygame.draw.circle(window, yellow, (200,250), 50)
    sleep(.3)
    pygame.display.update()
    pygame.draw.circle(window, green, (200,250), 50)
    sleep(.3)
    pygame.display.update()
    pygame.draw.circle(window, blue, (200,250), 50)
    sleep(.3)
    pygame.display.update()
    pygame.draw.circle(window, indigo, (200,250), 50)
    sleep(.3)
    pygame.display.update()
    pygame.draw.circle(window, violet, (200,250), 50)
    sleep(.3)
    pygame.display.update()
    
def greyCycle():
    global x,y,z
    if x > 0:
        pygame.draw.circle(window, (x, y, z), (200,250), 50)
        sleep(.001)
        pygame.display.update()
        x -= 1
        y -= 1
        z -= 1
        print x
    else:
        while x != 255:
            pygame.draw.circle(window, (x, y, z), (200,250), 50)
            sleep(.001)
            pygame.display.update()
            x += 1
            y += 1
            z += 1
            print x
        
while True:
    exitMessage("Press     to exit.")
    start()
    speedText('Slowest', .1275, .35)
    speedText('Slow', .2275, .35)
    speedText('Normal', .3275, .35)
    speedText('Fast', .428, .35)
    speedText('Fastest', .53, .35)
    events = pygame.event.get()
    for event in events:
        #add this chunk of code under existing loop from here
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_w:
                whichDir(green)
            elif event.key == pygame.K_a:
                whichDir(red)
            elif event.key == pygame.K_s:
                whichDir(blue)
            elif event.key == pygame.K_d:
                whichDir(yellow)
        elif event.type == pygame.KEYUP:
            whichDir(white)
        #to here
        #option to quit with x at top right
        elif event.type == pygame.QUIT:
            pygame.quit()
