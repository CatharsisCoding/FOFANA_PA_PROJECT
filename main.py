# abdel-malik fofana master 1 RSA
import pygame


pygame.init()

#background music
pygame.mixer.music.load("a.mp3")
pygame.mixer.music.play(-1)
var_pause=0


ecran = pygame.display.set_mode((640, 250))
bg = pygame.image.load("a.jpg")
continuer = True

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                continuer = False
            if event.key == pygame.K_m:
                if var_pause==0:
                    pygame.mixer.music.pause()
                    var_pause=1
                else:
                    pygame.mixer.music.unpause()
                    var_pause=0
    
    pygame.display.flip()

pygame.quit()

