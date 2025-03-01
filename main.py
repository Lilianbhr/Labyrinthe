from classes import *
import pygame
pygame.init()

# fenêtre
screen = pygame.display.set_mode((largeur, hauteur))

def arriere_plan():
    fichier = open("labyrinthe.txt", "r")
    lignes = fichier.readlines()
    y =0
    for ligne in lignes :
        x = 0
        for tuille in ligne :
            if tuille == "M" :
                mur = Mur(x, y)
                murs.add(mur)
                total.add(mur)
            x += 30
        y += 30

def afficher_score():
    background = pygame.Surface((largeur, score_hauteur))
    background.fill(noir)
    background.convert()
    image = pygame.image.load("assets/images/confiture.png").convert_alpha()
    image = pygame.transform.scale(image, (30, 30))
    image_pos = image.get_rect(left=9 * largeur / 10, centery=score_hauteur / 2 - 3)
    background.blit(image, image_pos)
    font = pygame.font.Font("assets/police/Poppins-Regular.ttf", 24)
    texte = font.render(f"{player.score}", 1, blanc)
    txt_pos = texte.get_rect(right=9 * largeur / 10 - 5, centery=score_hauteur / 2)
    background.blit(texte, txt_pos)
    tps = font.render(player.chrono.Timer.strftime("%M:%S"), 1, blanc)
    tps_pos = tps.get_rect(centerx = 2 * largeur / 4, centery = score_hauteur / 2)
    background.blit(tps, tps_pos)
    screen.blit(background, (0, hauteur - score_hauteur))

arriere_plan()

player = Player()
for t in range(5):
    confiture = Confiture()
masque = Masque(player.rect.centerx, player.rect.centery)

clock = pygame.time.Clock()
running = True
while running :
    player.update()
    masque.rect.center = player.rect.center
    screen.fill(blanc)
    total.draw(screen)
    afficher_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                player.direction = "H"
                break
            elif event.key == pygame.K_DOWN :
                player.direction = "B"
                break
            elif event.key == pygame.K_RIGHT :
                player.direction = "D"
                break
            elif event.key == pygame.K_LEFT :
                player.direction = "G"
                break
    dt = clock.tick(60)
    player.chrono.update(dt)
    pygame.display.flip()

pygame.quit()