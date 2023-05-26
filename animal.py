import pygame

class Animal(pygame.sprite.Sprite):
    def __init__(self, animal_x, animal_y, walk):
        self.animal_x = animal_x
        self.animal_y = animal_y
        self.walkCount = 0
        self.walk = walk
        self.vel = 5
        self.animal_image = ""

    def move(self):
        self.animal_x -= self.vel

        if self.walkCount >= 18:
            self.walkCount = 0
        else:
            self.animal_image = self.walk[self.walkCount // 3]
            self.walkCount += 1
        return self.animal_image