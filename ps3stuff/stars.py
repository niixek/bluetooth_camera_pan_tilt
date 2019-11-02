import pygame
from random import randrange

MAX_STARS = 250
STAR_SPEED = 2

def init_stars(screen):
    global stars
    stars = []
    for i in range(MAX_STARS):
        star = [randrange(0, screen.get_width() - 1),
                randrange(0, screen.get_height() - 1)]
        stars.append(star)

def draw(screen):
    global stars
    for star in stars:
        star[1] += STAR_SPEED
        if star[1] >= screen.get_height():
            star[1] = 0
            star[0] = randrange(0, 639)
        screen.set_at(star, (255,255,255))

def main():
    pygame.init()
    screen = pygame.display.set_mode((700,400))
    pygame.display.set_caption("yeet")
    clock = pygame.time.Clock()

    init_stars(screen)

    while True:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((0,0,0))
        draw(screen)
        pygame.display.flip()

main()
