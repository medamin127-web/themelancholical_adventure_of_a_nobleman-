import pygame
import spritesheet


class Player(pygame.sprite.Sprite):
        def __init__(self ,y):
            super().__init__()
            self.right = [pygame.transform.scale(pygame.image.load("assets/right/1.png"), (84.5, 87.1)),
                     pygame.transform.scale(pygame.image.load("assets/right/2.png"), (84.5, 87.1)),
                     pygame.transform.scale(pygame.image.load("assets/right/3.png"), (84.5, 87.1)),
                     pygame.transform.scale(pygame.image.load("assets/right/4.png"), (84.5, 87.1)),
                     pygame.transform.scale(pygame.image.load("assets/right/5.png"), (84.5, 87.1)),
                     pygame.transform.scale(pygame.image.load("assets/right/6.png"), (84.5, 87.1)),
                     pygame.transform.scale(pygame.image.load("assets/right/7.png"), (84.5, 87.1)),
                     pygame.transform.scale(pygame.image.load("assets/right/8.png"), (84.5, 87.1)),
                     pygame.transform.scale(pygame.image.load("assets/right/9.png"), (84.5, 87.1))]

            self.left = [pygame.transform.scale(pygame.image.load("assets/left/1.png"), (84.5, 87.1)),
                    pygame.transform.scale(pygame.image.load("assets/left/2.png"), (84.5, 87.1)),
                    pygame.transform.scale(pygame.image.load("assets/left/3.png"), (84.5, 87.1)),
                    pygame.transform.scale(pygame.image.load("assets/left/4.png"), (84.5, 87.1)),
                    pygame.transform.scale(pygame.image.load("assets/left/5.png"), (84.5, 87.1)),
                    pygame.transform.scale(pygame.image.load("assets/left/6.png"), (84.5, 87.1)),
                    pygame.transform.scale(pygame.image.load("assets/left/7.png"), (84.5, 87.1)),
                    pygame.transform.scale(pygame.image.load("assets/left/8.png"), (84.5, 87.1)),
                    pygame.transform.scale(pygame.image.load("assets/left/9.png"), (84.5, 87.1))]

            # jumping
            self.sprite_sheet_image3 = pygame.image.load("assets/jumping.png").convert_alpha()

            # fighting

            sprite_sheet_image4 = pygame.image.load("assets/fight.png").convert_alpha()

            # standing
            char = pygame.image.load("assets/standing.png").convert_alpha()

            self.sprite_sheet3 = spritesheet.SpriteSheet(self.sprite_sheet_image3)
            self.animation_list4 = [pygame.image.load("assets/fighting_sequence/4.png"),
                               pygame.image.load("assets/fighting_sequence/5.png"),
                               pygame.image.load("assets/fighting_sequence/6.png")]

            self.dead_animation = [pygame.image.load("assets/dead/1.png"),
                              pygame.image.load("assets/dead/2.png"),
                              pygame.image.load("assets/dead/3.png"),
                              pygame.image.load("assets/dead/4.png"),
                              pygame.image.load("assets/dead/5.png"),
                              pygame.image.load("assets/dead/6.png")]

            self.isjump = False
            self.up_key = False
            self.fight = False
            self.verify = False
            self.jumpCount = 10
            self.double = 1
            self.y_add = 0
            self.y_minus = 0
            self.move_right = False
            self.move_left = False
            self.walkCount = 0
            self.walkCount2 = 0
            self.vel = 6
            self.x = 70
            self.y = y
            self.y_modified = 0
            self.start_time = None
            self.counter = 0
            self.image = pygame.image.load ("assets/standing.png")
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            self.rect.height = 82
            self.display = False
            self.alive = True
            self.y_add = 0
            self.fallen = False
            self.fall = False
            self.jump_off_uppergound = False
            # Set the delay time (in milliseconds)
            self.delay_time = 60
            new_surface = pygame.transform.scale(char, (84.5, 87.1))
            rect = new_surface.get_rect()

        def move(self,SCREEN, scroll_x,ground_rect,ground_rect2):

                if self.alive:
                    # navigating through backgrounds
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                self.up_key = True
                                self.move_right = False
                                self.move_left = False
                                self.walkCount = 0

                    # Check if the right arrow key is being pressed
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_RIGHT]:
                        self.x += self.vel
                        self.move_right = True
                        self.move_left = False
                        self.rect.x = self.x + scroll_x
                    elif keys[pygame.K_LEFT]:
                        self.x -= self.vel
                        self.move_left = True
                        self.move_right = False
                        self.rect.x = self.x + scroll_x

                    else:
                        self.move_right = False
                        self.move_left = False
                        self.walkCount = 0

                    if not self.isjump:
                        if keys[pygame.K_SPACE]:
                            self.isjump = True
                            self.move_right = False
                            self.move_left = False
                            self.walkCount = 0
                            self.double = 1.9
                            if self.jumpCount == -15:
                                self.jumpCount = 10
                            self.jumpCount = self.jumpCount * self.double
                        if self.up_key:
                            self.isjump = True
                            self.move_right = False
                            self.move_left = False
                            self.walkCount = 0
                            self.double = 1
                    if not self.isjump:
                        if (self.jumpCount == -15 and (not self.rect.colliderect(ground_rect) )
                                or ( self.jumpCount == -17 and  not self.rect.colliderect(ground_rect2)) ) :
                            self.fall = True
                            self.jump_off_uppergound = True
                        if self.fall:
                            self.y -= self.jumpCount * 2
                            self.rect.y = self.y
                            self.jumpCount -= 1
                            if self.jumpCount < -10 * self.double:
                                self.jumpCount = 10
                                self.fall = False
                                self.up_key = False
                    if self.isjump:
                            self.y -= self.jumpCount * 2
                            self.rect.y = self.y
                            self.jumpCount -= 1

                            if self.jumpCount <4 and (self.rect.colliderect(ground_rect) or self.rect.colliderect(ground_rect2))  :
                                self.isjump = False

                            if self.jumpCount < -10 * self.double:
                                if self.y == 400:
                                    self.y = 570
                                    self.rect.y = self.y
                                    self.isjump = False
                                else:
                                    self.isjump = False
                                    self.jumpCount = 10
                                    self.up_key = False

                    if self.walkCount + 1 >= 27:
                        self.walkCount = 0
                    if self.move_right:
                        self.image = self.right[self.walkCount // 3]
                        self.walkCount += 1
                    elif self.move_left:
                        self.image = self.left[self.walkCount // 3]
                        self.walkCount += 1
                if not self.fight:
                    SCREEN.blit(self.image, (self.x + scroll_x, self.y))

        def fighting(self,SCREEN,scroll_x):
          if self.alive:
                if self.fight:
                    # Get the current time in milliseconds
                    if self.walkCount2 < 6:
                        new_surface = pygame.transform.scale(self.animation_list4[self.walkCount2//3], (115, 87.1))
                        self.walkCount2 += 1
                        return SCREEN.blit(new_surface, (self.x + scroll_x, self.y))
                    else:
                        self.walkCount2 = 0

                    # goblin.should_disappear = True
                    self.fight = False

                if not self.fight:
                        standing = pygame.image.load("assets/standing.png")
                        stand = pygame.transform.scale(standing, (84, 87))
                        self.image = stand

        def dead(self,SCREEN):
            self.image = self.dead_animation[5]
            self.y = 600

        def collisionwithobject(self, object_rect):
            if self.rect.colliderect(object_rect):
                self.y += 10

            if self.y == 720:
               self.alive = False
               return True



