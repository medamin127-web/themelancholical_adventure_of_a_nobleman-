import pygame, sys
import spritesheet
from pygame_functions import *
import enemy
import player
import animal

from button import Button

pygame.init()

SCREEN = SCREENSize(1280, 720)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/kingdom.png")

# get the current screen size
screen_width, screen_height = SCREEN.get_size()

# resize the image to fit the screen
image = pygame.transform.scale(BG, (screen_width, screen_height))

pygame.mixer.init()

pygame.mixer.music.load('assets/music.mp3')

# Start playing the music
pygame.mixer.music.play(-1)

# walking right

walk = [pygame.transform.scale(pygame.image.load("assets/enemies/enemy1/walk/1.png"), (130, 120)),
        pygame.transform.scale(pygame.image.load("assets/enemies/enemy1/walk/2.png"), (130, 120)),
        pygame.transform.scale(pygame.image.load("assets/enemies/enemy1/walk/3.png"), (130, 120)),
        pygame.transform.scale(pygame.image.load("assets/enemies/enemy1/walk/4.png"), (130, 120)),
        pygame.transform.scale(pygame.image.load("assets/enemies/enemy1/walk/11.png"), (130, 120)),
        pygame.transform.scale(pygame.image.load("assets/enemies/enemy1/walk/12.png"), (130, 120)),
        ]
walk2 = [
        pygame.transform.scale(pygame.image.load("assets/enemies/enemy2/walk/1.png"), (130, 120)),
        pygame.transform.scale(pygame.image.load("assets/enemies/enemy2/walk/2.png"), (130, 120)),
        pygame.transform.scale(pygame.image.load("assets/enemies/enemy2/walk/3.png"), (130, 120)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy2/walk/4.png"), (130, 120)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy2/walk/5.png"), (130, 120)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy2/walk/6.png"), (130, 120)),
         ]

walk3 = [
    pygame.transform.scale(pygame.image.load("assets/enemies/enemy3/walk/1.png"), (130, 120)),
    pygame.transform.scale(pygame.image.load("assets/enemies/enemy3/walk/2.png"), (130, 120)),
    pygame.transform.scale(pygame.image.load("assets/enemies/enemy3/walk/3.png"), (130, 120)),
    pygame.transform.scale(pygame.image.load("assets/enemies/enemy3/walk/4.png"), (130, 120)),
    pygame.transform.scale(pygame.image.load("assets/enemies/enemy3/walk/5.png"), (130, 120)),
    pygame.transform.scale(pygame.image.load("assets/enemies/enemy3/walk/6.png"), (130, 120))]

walk4 = [pygame.image.load("assets/animals/bird1/6.png"),
         pygame.image.load("assets/animals/bird1/5.png"),
         pygame.image.load("assets/animals/bird1/4.png"),
         pygame.image.load("assets/animals/bird1/3.png"),
         pygame.image.load("assets/animals/bird1/2.png"),
         pygame.image.load("assets/animals/bird1/1.png")]

walk5 = [pygame.image.load("assets/animals/bird2/6.png"),
         pygame.image.load("assets/animals/bird2/5.png"),
         pygame.image.load("assets/animals/bird2/4.png"),
         pygame.image.load("assets/animals/bird2/3.png"),
         pygame.image.load("assets/animals/bird2/2.png"),
         pygame.image.load("assets/animals/bird2/1.png")]

walk6 = [pygame.transform.scale(pygame.image.load("assets/enemies/enemy4/6.png"), (200, 159)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy4/5.png"), (200, 159)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy4/4.png"), (200, 159)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy4/3.png"), (200, 159)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy4/2.png"), (200, 159)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy4/1.png"), (200, 159))
         ]

walk7 = [pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/walk/9.png"), (120, 132)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/walk/8.png"), (120, 132)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/walk/7.png"), (120, 132)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/walk/6.png"), (120, 132)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/walk/5.png"), (120, 132)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/walk/4.png"), (120, 132)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/walk/3.png"), (120, 132)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/walk/2.png"), (120, 132)),
         pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/walk/1.png"), (120, 132))]

attack = [pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/attack/1.png"), (120, 132)),
          pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/attack/2.png"), (120, 132)),
          pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/attack/3.png"), (120, 132)),
          pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/attack/4.png"), (120, 132)),
          pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/attack/5.png"), (120, 132)),
          pygame.transform.scale(pygame.image.load("assets/enemies/enemy5/attack/6.png"), (120, 132)),
          ]

attack2 = [pygame.transform.scale(pygame.image.load("assets/enemies/witch/attack/1.png"), (85, 67)),
           pygame.transform.scale(pygame.image.load("assets/enemies/witch/attack/2.png"), (85, 67)),
           pygame.transform.scale(pygame.image.load("assets/enemies/witch/attack/3.png"), (85, 67)),
           pygame.transform.scale(pygame.image.load("assets/enemies/witch/attack/4.png"), (85, 67))]

walk8 = [
    pygame.transform.scale(pygame.image.load("assets/enemies/witch/idle/1.png"), (80, 97)),
    pygame.transform.scale(pygame.image.load("assets/enemies/witch/idle/2.png"), (80, 97)),
    pygame.transform.scale(pygame.image.load("assets/enemies/witch/idle/3.png"), (80, 97)),
    pygame.transform.scale(pygame.image.load("assets/enemies/witch/idle/4.png"), (80, 97)),
    pygame.transform.scale(pygame.image.load("assets/enemies/witch/idle/5.png"), (80, 97)),
    pygame.transform.scale(pygame.image.load("assets/enemies/witch/idle/6.png"), (80, 97)),
    pygame.transform.scale(pygame.image.load("assets/enemies/witch/idle/7.png"), (80, 97))]

monster1_stand = pygame.transform.scale(pygame.image.load("assets/enemies/enemy4/1.png"), (200, 159))
final_boss_stand = pygame.transform.scale(pygame.image.load("assets/enemies/enemy2/walk/1.png"), (120, 132))
princess = pygame.transform.scale(pygame.image.load("assets/princess_stand.png"), (85, 95))

flames = [pygame.image.load("assets/flames/fire1.png"),
          pygame.image.load("assets/flames/Fire2.png"),
          pygame.image.load("assets/flames/Fire3.png"),
          pygame.image.load("assets/flames/Fire4.png"),
          pygame.image.load("assets/flames/Fire5.png"),
          pygame.image.load("assets/flames/Fire6.png")]

# door
door_image = "assets/door.png"
door = pygame.image.load(door_image).convert_alpha()

clock = pygame.time.Clock()

BLACK = (0, 0, 0)


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def get_font2(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/KGHAPPY.ttf", size)


def play():
    last_update = pygame.time.get_ticks()
    isjump = False
    up_key = False
    fight = False
    verify = False
    jumpCount = 10
    double = 1
    y_add = 0
    y_minus = 0
    move_right = False
    move_left = False
    walkCount = 0
    vel = 6
    x = 70
    y = 570
    y_modified = 0
    sprite_alive = True
    sprite_died = False
    death_time = None
    collision = False
    move_right = True
    victory = False
    lives = 3
    exist = False
    flame_image = None

    flame_width = flames[0].get_width()
    flame_height = 71

    flame_animations = [
        {"count": 0, "position": (200, 520)},
        {"count": 0, "position": (250, 520)},
        {"count": 0, "position": (300, 520)},
        {"count": 0, "position": (350, 520)},
        {"count": 0, "position": (400, 520)},
        {"count": 0, "position": (450, 520)},
        {"count": 0, "position": (500, 520)},
        {"count": 0, "position": (550, 520)},
        {"count": 0, "position": (600, 520)},
        {"count": 0, "position": (650, 520)},
        {"count": 0, "position": (700, 520)}

    ]

    # Calculate the bounding rectangle for all flame animations
    flame_rects = [pygame.Rect(animation["position"], (flame_width, flame_height)) for animation in flame_animations]
    bounding_rect = flame_rects[0].unionall(flame_rects[1:])
    bounding_rect.y = 590
    counter = 0

    # create a pitfall
    hole_width = 158
    hole_height = 124
    hole_surface = pygame.Surface((hole_width, hole_height))

    hole_color = "#19272b"
    hole_surface.fill(hole_color)
    hole_surface2 = pygame.Surface((hole_width + 400, hole_height + 10))
    hole_surface2.fill(hole_color)
    hole_rect = hole_surface.get_rect()
    hole_rect2 = hole_surface2.get_rect()

    # create spikes in pitfall
    spikes = pygame.image.load("assets/spikes.png")

    # create items in the game
    signboard = pygame.image.load("assets/Signboard.png")
    house = pygame.image.load("assets/house.png")
    tree = pygame.image.load("assets/tree.png")
    tree2 = pygame.image.load("assets/tree2.png")
    block = pygame.image.load("assets/block.png")
    upper_ground = pygame.transform.scale(pygame.image.load("assets/ground.png"), (290, 37))
    upper_ground_small = pygame.image.load("assets/ground.png")
    castle = pygame.transform.scale(pygame.image.load("assets/castle.png"), (395, 346))
    upper_ground_rect = upper_ground.get_rect()
    block_rect = block.get_rect()

    block_rect.y = 647
    upper_ground_rect.y = 480
    add_to_block = 0
    # Make the block's rect match the dimensions of the block's image
    block_rect.width = block.get_width()
    block_rect.height = block.get_height()

    # Make the upper grounds rect match the dimensions of the upper ground image
    upper_ground_rect.width = upper_ground.get_width()
    upper_ground_rect.height = upper_ground.get_height() - 40

    character_image = ""

    # Define timing variables
    freeze_time = 3000  # 3 seconds
    start_time = pygame.time.get_ticks()

    img = pygame.image.load('assets/gamebackground.png')
    img1 = pygame.image.load('assets/gamebackground.png')

    # scrolling setups
    scroll_x = 0
    bg_width = img.get_width()

    # instance of enemy class
    goblin = enemy.Enemy(1200, 555, 100, 120, 10, walk)
    creature = enemy.Enemy(2200, 555, 100, 120, 10, walk3)
    monster = enemy.Enemy(4090, 527, 200, 159, 10, walk6)
    monster2 = enemy.Enemy(4690, 543, 200, 159, 10, walk7)
    witch = enemy.Enemy(5130, 565, 100, 120, 10, walk8)
    final_boss = enemy.Enemy(6650, 550, 100, 120, 10, walk2 )

    # instance of animal class
    bird1 = animal.Animal(1000, 250, walk4)
    bird2 = animal.Animal(800, 190, walk5)

    # npc characters

    woman = pygame.transform.scale(pygame.image.load('assets/women.png'), (130, 120))

    enemies = [
        goblin,
        creature,
        monster,
        monster2,
        witch,
        final_boss
    ]

    higher_ground = [
        upper_ground_small,
        upper_ground_small,
        upper_ground_small,
        upper_ground_small,
        upper_ground_small,
        upper_ground_small,
        upper_ground_small,
        upper_ground_small,
    ]

    higher_ground_height = upper_ground_small.get_height()
    higher_ground_width = upper_ground_small.get_width() * (len(higher_ground) - 1) - 20
    rect_x = 200
    rect_y = 520
    higher_ground_rect = pygame.Rect(rect_x, rect_y, higher_ground_width, higher_ground_height)

    this_enemy = 0

    # instance of player
    sprite = player.Player(570)

    screen_width, screen_height = pygame.display.get_surface().get_size()

    # pausing graphics
    is_paused = False
    pause_font = pygame.font.SysFont(None, 30)
    pause_text = pause_font.render("Game Paused", True, (255, 255, 255))
    pause_rect = pause_text.get_rect(center=(screen_width // 2, screen_height // 2))
    font = pygame.font.Font(None, 53)

    while True:
        clock.tick(27)

        lives_text = font.render(f"x{lives}", True, pygame.Color("white"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if sprite.alive:
                        sprite.fight = True

                if event.key == pygame.K_p:
                    is_paused = not is_paused
        p = 0

        if not is_paused:

            # Update scroll position based on character position
            if sprite.x >= 800:
                scroll_x = -(sprite.x - 800)
            if scroll_x > -(bg_width - 1280):
                scroll_x = -(bg_width - 1280)

            # blitting stuff on the screen
            SCREEN.blit(img, (scroll_x, 0))
            SCREEN.blit(img1, (scroll_x + 1280, 0))
            SCREEN.blit(img1, (scroll_x + 2560, 0))
            SCREEN.blit(img1, (scroll_x + 3840, 0))
            SCREEN.blit(img1, (scroll_x + 5120, 0))
            SCREEN.blit(img1, (scroll_x + 6400, 0))

            SCREEN.blit(woman, (scroll_x + 2660, 560))
            SCREEN.blit(house, (scroll_x + 2770, 453))
            SCREEN.blit(tree, (scroll_x + 295, 453))
            SCREEN.blit(tree2, (scroll_x + 2980, 453))
            SCREEN.blit(signboard, (955 + scroll_x, 538))
            SCREEN.blit(hole_surface, (scroll_x + 1450, 640))
            SCREEN.blit(hole_surface2, (scroll_x + 3300, 640))
            SCREEN.blit(upper_ground, (scroll_x + 4990, 480))
            SCREEN.blit(castle, (scroll_x + 6500, 337))
            SCREEN.blit(princess, (scroll_x + 6800, 550))

            # setting up some items x position in relation with the scroll
            block_rect.x = scroll_x + 3300 + add_to_block
            upper_ground_rect.x = scroll_x + 4990
            higher_ground_rect.x = scroll_x + 5550
            bounding_rect.x = scroll_x + 5560

            if scroll_x <= -2000:
                SCREEN.blit(block, block_rect)

                # this will move the block right and left
                if move_right:
                    add_to_block += 5
                    if block_rect.x >= scroll_x + 3760:
                        move_right = False
                    if sprite.rect.colliderect(block_rect):
                        sprite.x += 5
                else:
                    add_to_block -= 5
                    if block_rect.x <= scroll_x + 3300:
                        move_right = True
                    if sprite.rect.colliderect(block_rect):
                        sprite.x -= 5

                # detecting collision with pitfalls
                if not sprite.rect.colliderect(block_rect):
                    sprite.collisionwithobject(hole_rect2)


            # set the position of the hole
            # first hole
            hole_rect.x = scroll_x + 1460
            hole_rect.y = 645
            hole_rect.width = 148

            # second_hole
            hole_rect2.x = scroll_x + 3320
            hole_rect2.y = 650

            # displaying the sprite's lives
            for i in range(lives):
                pic = pygame.image.load("assets/sprite_picture.png")
                p += 50
                SCREEN.blit(pic, (950 + p, 10))
            SCREEN.blit(lives_text, (955, 30))

            sprite.fighting(SCREEN, scroll_x)
            sprite.move(SCREEN, scroll_x, upper_ground_rect, higher_ground_rect)

            # displaying the enemies at certain time
            if sprite.x >= 1800:
                creature.animate(sprite.x, walk3)
                creature.draw2(SCREEN, scroll_x)

            if sprite.x >= 4200:
                monster2.draw4(SCREEN, scroll_x, sprite.x, attack)

            if sprite.x>= 5000:
                final_boss.draw3(SCREEN,scroll_x,sprite.x,final_boss_stand)
            witch.draw5(SCREEN, scroll_x, sprite.x)
            witch.attack_animation(SCREEN, scroll_x, attack2)

            monster.draw3(SCREEN, scroll_x, sprite.x, monster1_stand)
            goblin.draw(SCREEN, scroll_x)

            # displaying the animals and their methods
            SCREEN.blit(bird1.move(), (bird1.animal_x + scroll_x, 250))
            SCREEN.blit(bird2.move(), (bird2.animal_x + scroll_x, 190))

            # display flames
            pos = 0
            for animation in flame_animations:
                count = animation["count"]
                position = animation["position"]
                if count >= 30:
                    count = 0
                else:
                    flame_image = flames[count // 5]
                    SCREEN.blit(flame_image, (5550 + scroll_x + pos, 520))
                    count += 1
                    pos += 50

                animation["count"] = count
            c = 0
            # displaying the higher ground on top off the flames
            for upp_ground in higher_ground:
                SCREEN.blit(upp_ground, (5550 + c + scroll_x, 520))
                c += 80


            keys = pygame.key.get_pressed()

            # checks if there's a collision with an enemy:
            for enemie in enemies:
                if sprite.rect.colliderect(enemie.rect(scroll_x)):
                    collision = True
                    this_enemy = enemie
                    if enemie == final_boss:
                        victory = True


            if witch.attack_rect:
                if sprite.rect.colliderect(witch.attack_rect):
                    sprite.alive = False
                    sprite_died = True
                    sprite.dead(SCREEN)
                    witch.stop = True
            if sprite.rect.colliderect(bounding_rect):
                sprite.alive = False
                sprite_died = True
                sprite.dead(SCREEN)
            if collision and sprite.alive:
                if keys[pygame.K_s]:
                    this_enemy.enemy_x = -1000
                    collision = False
                else:
                    sprite.alive = False
                    sprite_died = True
                    sprite.dead(SCREEN)
                    this_enemy.stop = True
            if (sprite_died and sprite_alive) or sprite.collisionwithobject(hole_rect):
                sprite_alive = False
                death_time = pygame.time.get_ticks()

            if not sprite_alive:
                if death_time is not None:
                    time_since_death = pygame.time.get_ticks() - death_time
                    if time_since_death >= 3000:  # wait for 5 seconds
                        # reset game state and restart the game
                        sprite.x = 70
                        sprite.y = 570
                        sprite.rect.x = sprite.x
                        sprite_died = False
                        goblin.stop = False
                        witch.stop: False
                        goblin.enemy_x = 1200
                        bird1.animal_x = 1000
                        bird2.animal_x = 800
                        scroll_x = 0
                        goblin.enemy_rect.x = goblin.enemy_x
                        sprite.alive = True
                        sprite_alive = True
                        collision = False
                        lives -= 1
                        if lives == 0:
                            exist = True

        else:
            SCREEN.blit(pause_text, pause_rect)

        # the case where the lives are 0
        if exist:
            render_game_over_screen()
        if victory:
            won()
        pygame.display.update()


def won():
    # Create a Pygame surface with a black background

    SCREEN.fill(pygame.Color("black"))

    # Render game over message
    game_over_font = pygame.font.Font(None, 50)
    game_over_font2 = pygame.font.Font(None, 35)
    game_over_text = game_over_font.render("The End!", True, pygame.Color("white"))
    text = game_over_font2.render("You Rescued The Princess", True, pygame.Color("white"))
    img = pygame.image.load("assets/princess_happy.png")
    # Get the original size of the image
    original_size = img.get_size()

    # Scale the image
    new_size = (original_size[0] * 2.5, original_size[1] * 2.5)
    scaled_image = pygame.transform.scale(img, new_size)

    SCREEN.blit(game_over_text, (640 - 100, SCREEN.get_height() / 2 - 200))
    SCREEN.blit(scaled_image, (640 - 110, SCREEN.get_height() / 2 - 190))
    SCREEN.blit(text, (640 - 180, SCREEN.get_height() / 2))

    # Define button dimensions and position
    button_width = 170
    button_height = 50
    button_x = SCREEN.get_width() / 2 - 80
    button_y = SCREEN.get_height() / 2 + 100
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    # Define button appearance
    button_color = pygame.Color("blue")
    button_hover_color = pygame.Color("lightblue")
    button_text = "Play Again!"
    font = pygame.font.Font(None, 30)
    text_color = pygame.Color("white")
    text_surface = font.render(button_text, True, text_color)
    text_rect = text_surface.get_rect(center=(SCREEN.get_width() / 2 + 10, SCREEN.get_height() / 2 + 125))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                main_menu()

        # Draw button
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(SCREEN, button_hover_color, button_rect)
    else:
        pygame.draw.rect(SCREEN, button_color, button_rect)
    SCREEN.blit(text_surface, text_rect)

def render_game_over_screen():
    # Create a Pygame surface with a black background

    SCREEN.fill(pygame.Color("black"))

    # Render game over message
    game_over_font = pygame.font.Font(None, 50)
    game_over_font2 = pygame.font.Font(None, 35)
    game_over_text = game_over_font.render("Game Over!", True, pygame.Color("white"))
    text = game_over_font2.render("You Failed To Rescue The Princess", True, pygame.Color("white"))
    img = pygame.image.load("assets/fail.png")
    # Get the original size of the image
    original_size = img.get_size()

    # Scale the image
    new_size = (original_size[0] * 2.5, original_size[1] * 2.5)
    scaled_image = pygame.transform.scale(img, new_size)

    SCREEN.blit(game_over_text, (640 - 100, SCREEN.get_height() / 2 - 200))
    SCREEN.blit(scaled_image, (640 - 70, SCREEN.get_height() / 2 - 190))
    SCREEN.blit(text, (640 - 180, SCREEN.get_height() / 2))

    # Define button dimensions and position
    button_width = 170
    button_height = 50
    button_x = SCREEN.get_width() / 2 - 80
    button_y = SCREEN.get_height() / 2 + 100
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    # Define button appearance
    button_color = pygame.Color("blue")
    button_hover_color = pygame.Color("lightblue")
    button_text = "Play Again!"
    font = pygame.font.Font(None, 30)
    text_color = pygame.Color("white")
    text_surface = font.render(button_text, True, text_color)
    text_rect = text_surface.get_rect(center=(SCREEN.get_width() / 2 + 10, SCREEN.get_height() / 2 + 125))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                main_menu()

        # Draw button
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(SCREEN, button_hover_color, button_rect)
    else:
        pygame.draw.rect(SCREEN, button_color, button_rect)
    SCREEN.blit(text_surface, text_rect)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("asset")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:

        SCREEN.blit(image, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font2(45).render("The melancholic Adventure Of A Nobleman"
                                         , True, "#b68f40")

        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            # draw the current frame of the video to the screen

        # update the screen
        pygame.display.flip()


main_menu()
