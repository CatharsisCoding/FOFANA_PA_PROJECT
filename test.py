# abdel-malik fofana master 1 RSA
import pygame
import sys


pygame.init()

#fps managing
clock = pygame.time.Clock()
fps = int(sys.argv[1])


#background music
pygame.mixer.music.load("a.mp3")
pygame.mixer.music.play(-1)
music_pause=0


#screen option
ecran = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Maliki-fencing®")

#load background from file
bg_name="c.jpg"

#fonction for drawing background on screen
def display_bg(bg_name):
    ecran.blit(pygame.image.load(bg_name).convert_alpha(),(0,0))

#option writing something in the screen
police =pygame.font.SysFont("Arialblack",40) #font
color_text=(0,0,0) #black color
def texte(texte,police,couleur,x,y):
    img=police.render(texte,True,couleur)
    ecran.blit(img,(x,y))

continuer = True
while continuer:

    #bg display
    display_bg(bg_name)
    #text display
    texte('appuyer sur "m" pour éteindre la musique',police ,color_text,0,25)
    texte("appuyer sur echap pour quitter",police ,color_text,0,0)
    #fps display
    clock.tick(fps)
    texte(str(round(clock.get_fps(),2)),police,(255, 255, 0),1300,0)

    for event in pygame.event.get():
        #if we touch a key we do something:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
            if event.key == pygame.K_m:
                bg_name="b.jpg"
                if music_pause==0:
                    pygame.mixer.music.pause()
                    music_pause=1
                else:
                    pygame.mixer.music.unpause()
                    music_pause=0
            if event.key == pygame.K_p:
                game_pause=True
        if event.type == pygame.QUIT:
            continuer=False
    
    pygame.display.update()

pygame.quit()

