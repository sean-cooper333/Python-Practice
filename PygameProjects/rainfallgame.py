# Importing libraries
import pygame
import time
import random
pygame.font.init()

# Setting window w/h
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Giving the window a name
pygame.display.set_caption("Space Dodge")

# setting the background and making it scale to the window using bg.jpeg image
BG = pygame.transform.scale(pygame.image.load(
    "bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40

PLAYER_HEIGHT = 60

PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)

STAR_WIDTH = 10

STAR_HEIGHT = 20

STAR_VEL = 5

# The `draw` function in Python updates the display with a background image in a Pygame window.


def draw(player, elapsed_time, stars):

    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()

# The main function runs a game loop that continuously checks for events and updates the game until
# the user quits.


def main():
    run = True

    # setting player character to a rectangle, setting start coords. x, y subtracting player height to generate position dynamically
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    # create clock object
    clock = pygame.time.Clock()
    # get current time
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = random.randint(20, 2000)
    star_count = 0

    stars = []

    hit = False

    while run:
        # returning amount of milliseconds since the last tick(60)
        star_count += clock.tick(60)
        # set to run at 60fps
        clock.tick(60)

        # storing time we start the while loop, then every time we iterate we are getting what the current time is and subtracting that from the start timm which will give us the elapsed time from when we started the while loop

        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            # do something x amount of times times
            for _ in range(5):
                # picking random position on x axis for star to generate
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                # starts near top of screen then falls down screen
                star = pygame.Rect(star_x, - STAR_HEIGHT,
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

              # gets keys and tells you if the player has pressed them
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
                # check if player is struck by star
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width() /
                     2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()
