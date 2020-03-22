import pygame

pygame.init()

# Size of our Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy Game'

# Colors used to fill background until pics come
white = (255, 255, 255)
black = (0, 0, 0)

# Clock used to update game events and frames
clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False

# Initializing the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)


while not is_game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

        print(event)

    screen.fill(white)
    pygame.draw.rect(screen, black, [400, 400, 100, 100])

    # update game graphics
    pygame.display.update()

    # Tick the clock to update everything within the game
    clock.tick(TICK_RATE)

pygame.quit()
quit()