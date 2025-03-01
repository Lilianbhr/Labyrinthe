from generale import *
from random import *
from datetime import timedelta, datetime, date, time
import pygame

class Mur(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/mur.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (taille_tuiles, taille_tuiles))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        murs.add(self)
        total.add(self)

class Confiture(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/confiture.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (taille_tuiles, taille_tuiles))
        self.rect = self.image.get_rect()
        continuer = True
        while continuer :
            self.rect.x = randint(1, 20) * taille_tuiles
            self.rect.y = randint(1, 20) * taille_tuiles
            liste_collision = pygame.sprite.spritecollide(self, total, False)
            if len(liste_collision) < 1 :
                continuer = False
        confiture.add(self)
        total.add(self)

class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (taille_tuiles, taille_tuiles))
        self.rect = self.image.get_rect()
        continuer = True
        while continuer:
            self.rect.x = randint(1, 20) * taille_tuiles
            self.rect.y = randint(1, 20) * taille_tuiles
            liste_collision = pygame.sprite.spritecollide(self, total, False)
            if len(liste_collision) < 1:
                continuer = False
        self.direction = "-"
        self.score = 0
        self.chrono = Chrono()
        total.add(self)

    def update(self):
        prec_x = self.rect.x
        prec_y = self.rect.y

        if self.direction == "H" :
            self.rect.y -= taille_tuiles
        elif self.direction == "B" :
            self.rect.y += taille_tuiles
        elif self.direction == "D" :
            self.rect.x += taille_tuiles
        elif self.direction == "G" :
            self.rect.x -= taille_tuiles

        liste_collision = pygame.sprite.spritecollide(self, total, False)
        for elt in liste_collision :
            if type(elt) == Mur :
                self.rect.x = prec_x
                self.rect.y = prec_y
            elif type(elt) == Confiture :
                elt.kill()
                self.score += 1

        if self.score == 5 :
            self.chrono.stop()

        self.direction = "-"

class Masque(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/masque.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        total.add(self)

class Chrono :
    def __init__(self):
        self.Timer = datetime.combine(date.today(), time(0, 0))
        self.Stop = False

    def stop(self):
        self.Stop = True

    def update(self, dt):
        if not self.Stop :
            self.Timer += timedelta(milliseconds=dt)