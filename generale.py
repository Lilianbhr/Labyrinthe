import pygame

# groupes
murs = pygame.sprite.Group()
total = pygame.sprite.Group()
confiture = pygame.sprite.Group()

# variables
taille_tuiles = 30
nb_tuilles = 21
score_hauteur = 100
hauteur = nb_tuilles * taille_tuiles + score_hauteur
largeur = nb_tuilles * taille_tuiles

# couleurs
blanc = pygame.Color(255, 255, 255)
noir = pygame.Color(0, 0, 0)