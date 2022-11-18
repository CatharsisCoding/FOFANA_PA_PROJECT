import curses 
from random import randint
import pygame
import sys
import time
from threading  import Timer

pygame.init()

#fps managing
clock = pygame.time.Clock()
fps = int(sys.argv[1])


#background music
#pygame.mixer.music.load("sound/a.mp3")
#pygame.mixer.music.play(-1)
#music_pause=0


#constants

WINDOW_WIDTH = 60 
WINDOW_HEIGHT = 20 

# setup window
curses.initscr()
win = curses.newwin(WINDOW_HEIGHT, WINDOW_WIDTH, 0, 0) # rows, columns
win.keypad(1) #easier to process keypad on terminal
curses.noecho() #instant key process
curses.curs_set(0) #hide the "cursor" in terminal
win.border(0,0,0,"#",0,0,0,0) #draw border
win.nodelay(1) # -1

#load scene frop .ffscene file
def load_scene(namefile):
    with open(namefile) as my_file:
        scene=my_file.read()
    #bug fix when rendering i fix the bug that way i dont know how but it work so i keep it that way :) 
    list1=list(scene)
    list1.pop()
    scene=""
    return scene.join(list1)
current_scene=load_scene("ffscene/default.ffscene")

# game logic
score = [0,0]
print(score[1])
ESC = 27 #ascii
key=curses.has_key(97)
weapon_p1="/"
weapon_p2="\\"
x1=0
y1=0
x2=0
y2=0
def player1():
    #player1 display
    win.addstr(14+y1, 1+x1, "<o>") 
    win.addstr(15+y1, 2+x1, "|_"+ weapon_p1) 
    win.addstr(16+y1, 2+x1, "|") 
    win.addstr(17+y1, 2+x1, "|") 
    win.addstr(18+y1, 1+x1, "/|")
def player2():
    #player2 display
    win.addstr(14+y2, 54+x2, "<o>") 
    win.addstr(15+y2, 53+x2, weapon_p2+"_|") 
    win.addstr(16+y2, 55+x2, "|") 
    win.addstr(17+y2, 55+x2, "|") 
    win.addstr(18+y2, 55+x2, '|\\') 
def clean():
    for i in range(12,19):
        for j in range(1,59):
            win.addstr(i,j," ")
def jump1_left():
   global y1
   y1+=1
def jump1_right():
   global y1 
   y1+=1
def jump2():
   global y2
   y2+=1

while key != ESC:

    #display player
    clean()

    player1()
    player2()
    #fps display
    clock.tick(fps)
    win.addstr(0, 45, "FPS: " +str(round(clock.get_fps(),2)))

    win.addstr(1, 22, "Score : "+str(score[0])+" | "+str(score[1])) #score display
    #win.addstr(19, 1, current_scene) #ffscene display



   

   
    key = win.getch()  #we wait for the next charactere
    #a 97 , q 113 , d 100 , i 105 , e 101 , m 109 , z 122,o 111
    #movement player 1
    if key == 97: #when we press a we jump (ascii 97)
        y1-=1
        x1-=2
        t=Timer(0.25,jump1_left)
        t.start()
    if key == 113: #press q go left
        x1-=1
    if key == 100: #press d go right
        x1+=1
    if key == 101:
        y1+=1
        x1+=2
        t=Timer(0.25,jump1_right)
        t.start()
    if key == curses.KEY_RIGHT:
        pass    
    #movement player 2
    if key == curses.KEY_DOWN: 
        y2+=1
    if key == curses.KEY_UP:
        y1-=1
        t=Timer(0.25,jump2)
        t.start()
    if key == curses.KEY_LEFT:
        pass
    if key == curses.KEY_RIGHT:
        pass    


    # check if we hit the border
   # if y == 0: break
    #if y == WINDOW_HEIGHT-1: break
    #if x == 0: break
    #if x == WINDOW_WIDTH -1: break



curses.endwin()
print(f"Final score = {score}")