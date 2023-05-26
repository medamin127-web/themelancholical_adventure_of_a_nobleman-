import pygame

class Enemy(pygame.sprite.Sprite):
    # walkingleft

    def __init__(self, enemy_x, enemy_y, height, width, end,walk):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.attack_x = self.enemy_x +10
        self.attack_y = self.enemy_y + 25
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.enemy_x, self.end]
        self.walkCount = 0
        self.walkCount2 = 0
        self.vel = 5
        self.enemy_image = pygame.transform.scale(pygame.image.load("assets/enemies/enemy3/walk/stand.png"), (130, 120))
        self.attack_image = pygame.transform.scale(pygame.image.load("assets/enemies/enemy3/walk/stand.png"), (130, 120))
        # Set up the flag variable
        self.should_disappear = False
        self.display = False
        self.attack = False
        self.enemy_rect = ""
        self.attack_rect = None
        self.walk = walk
        self.stop = False

    #moving enemy
    def draw(self, win,scroll_x):
        self.move()

        if not self.stop:
            if self.walkCount >= 18:
                self.walkCount = 0
            else:
                self.display = True
                self.enemy_image = self.walk[self.walkCount // 3]
                self.walkCount += 1
        if self.stop:
            self.enemy_image = pygame.transform.scale(pygame.image.load("assets/enemies/enemy1/walk/9.png"), (130, 120))
        if self.display:
            return win.blit(self.enemy_image, (self.enemy_x + scroll_x, self.enemy_y))

    def move(self):
        if not self.stop:
            self.enemy_x -= self.vel
        if self.enemy_x <= self.path[1] :
            self.should_disappear = True

    def rect(self, scroll_x):
        self.enemy_rect = self.enemy_image.get_rect()
        self.enemy_rect.x = self.enemy_x+20 + scroll_x
        self.enemy_rect.y = self.enemy_y
        self.enemy_rect.width = 80
        return self.enemy_rect

    def animate(self,sprite_x,walk):
        if self.enemy_x - sprite_x <= 200:
            if self.walkCount < len(walk)-1:
                self.walkCount += 1
            self.enemy_image = self.walk[self.walkCount]
        else:
            self.enemy_image = pygame.transform.scale(pygame.image.load("assets/enemies/enemy3/walk/stand.png"),
                                                      (130, 120))
            self.walkCount = 0

    #standing enemy
    def draw2(self,win,scroll_x):
        return win.blit(self.enemy_image,(self.enemy_x + scroll_x, self.enemy_y))

    #standing but attacking enemy
    def draw3(self,win,scroll_x,sprite_x,stand_image):
        if self.walkCount >= 24:
            self.walkCount = 0

        if 70 >= self.enemy_x - sprite_x >= -100:
            self.enemy_image = self.walk[self.walkCount // 4]
            self.walkCount += 1
        else:
            self.enemy_image = stand_image
        return win.blit(self.enemy_image, (self.enemy_x + scroll_x, self.enemy_y))

    def draw4(self,win,scroll_x,sprite_x,attack):

        if self.walkCount >= 18:
            self.walkCount = 0

        if 70 >= self.enemy_x - sprite_x >= -100:
            self.enemy_y = 553
            self.enemy_image = attack[self.walkCount // 3]
            self.walkCount += 1

        else:
            self.enemy_y = 543
            self.enemy_x -= self.vel
            self.enemy_image = self.walk[self.walkCount // 3]
            self.walkCount += 1
        return win.blit(self.enemy_image, (self.enemy_x + scroll_x, self.enemy_y))

    #magician
    def draw5(self,win,scroll_x,sprite_x):
        if self.stop:
            self.enemy_image = pygame.transform.scale(pygame.image.load("assets/enemies/witch/standing.png"), (80, 97))
        else:
            if self.walkCount >= 18:
                self.walkCount = 0
            if 300 >= self.enemy_x - sprite_x >= -50:
                self.attack = True
                self.enemy_image = self.walk[self.walkCount // 3]
                self.walkCount += 1

            else:
                self.attack = False
                self.walkCount2 = 0
                self.enemy_image = pygame.transform.scale(pygame.image.load("assets/enemies/witch/standing.png"), (80, 97))
        return win.blit(self.enemy_image,(self.enemy_x + scroll_x, self.enemy_y))

    def attack_animation(self, win, scroll_x, attack2):
        if not self.stop:
            if self.attack:
                if not self.walkCount2 >= 16:
                    self.attack_image = attack2[self.walkCount2 // 4]
                    self.walkCount2 += 1
                    self.attack_x -= self.vel + 10
                else:
                    self.walkCount2 = 0
                    self.attack_x = self.enemy_x + 10
                self.attack_rect = self.attack_image.get_rect()
                self.attack_rect.x = self.attack_x + scroll_x + 26
                self.attack_rect.y = self.attack_y+15
                self.attack_rect.width = 28
                self.attack_rect.height = 30
                return win.blit(self.attack_image,(self.attack_x + scroll_x, self.attack_y))
            else:
                self.walkCount2 = 0
                self.attack_x = self.enemy_x + 4

