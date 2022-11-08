# abdel-malik fofana master 1 RSA
import pygame


pygame.init()

#background music
pygame.mixer.music.load("a.mp3")
pygame.mixer.music.play()


ecran = pygame.display.set_mode((640, 250))
bg = pygame.image.load("a.jpg")
continuer = True

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                continuer = False
            if event.key == pygame.K_m:
                pygame.mixer.music.mute()
    
    pygame.display.flip()

pygame.quit()

