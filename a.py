import curses 
from random import randint
import pygame
import sys
import time
import threading
from threading  import Timer
from pynput.keyboard import *

pygame.init()

#fps managing
clock = pygame.time.Clock()
fps = int(sys.argv[1])


#background music
pygame.mixer.music.load("sound/a.mp3")
pygame.mixer.music.play(-1)
music_pause=0


#constants

WIDTH = 60 
HEIGHT = 20 

# setup window
curses.initscr()
win = curses.newwin(HEIGHT, WIDTH, 0, 0) # rows, columns
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
current_scene = current_scene.replace("_"," ")
wall=[]
for i in range(len(current_scene)):
    if(current_scene[i]=='x'):
        wall.append(i)







# game logic
score = [0,0]
ESC = 27 #ascii
key=curses.has_key(97)
weapon_p1=" "
weapon_p2=" "
rest_p1=" \\"
rest_p2="/ "
player1_attack=0
player2_attack=0
player1_block=0
player2_block=0
attack_speed= float(sys.argv[2])
blocking_speed= float(sys.argv[3])
movement_speed= int(sys.argv[4])


#x and y position of player 1
positionx_p1=1
positiony_p1=0
#x and y position of player 2
positionx_p2=55
positiony_p2=0

#print player 1 on screen
def player1():
    #player1 display
    win.addstr(14+positiony_p1, positionx_p1, "<o>") 
    win.addstr(15+positiony_p1, positionx_p1, " |_"+ weapon_p1) 
    win.addstr(16+positiony_p1, positionx_p1, " |"+rest_p1) 
    win.addstr(17+positiony_p1, positionx_p1, " |") 
    win.addstr(18+positiony_p1, positionx_p1, "/|")

#print player 2 on screen
def player2():
    #player2 display
    win.addstr(14+positiony_p2, positionx_p2, " <o>") 
    win.addstr(15+positiony_p2, positionx_p2, weapon_p2+"_|") 
    win.addstr(16+positiony_p2, positionx_p2,"  |") , win.addstr(16+positiony_p2, positionx_p2, rest_p2) 
    win.addstr(17+positiony_p2, positionx_p2, "  |") 
    win.addstr(18+positiony_p2, positionx_p2+2, '|\\') 

#clean the screen
def clean():
    for i in range(1,19):
        for j in range(1,59):
            win.addstr(i,j," ")

def jump1():
   global positiony_p1 
   positiony_p1+=1
def jump2():
   global positiony_p2
   positiony_p2+=1

def move_left_p1():
    global positionx_p1
    positionx_p1-=1
def move_left_p2():   
    global positionx_p2
    positionx_p2-=1
def move_right_p1():
    global positionx_p1
    positionx_p1+=1
def move_right_p2():
    global positionx_p2
    positionx_p2+=1
def switch_weapon_p1():
   global rest_p1
   global weapon_p1
   global player1_attack
   global player1_block
   player1_attack=0
   player1_block=0
   rest_p1=" \\"
   weapon_p1=" "
def switch_weapon_p2():
   global rest_p2 
   global weapon_p2
   global player2_attack
   global player2_block
   player2_attack=0
   player2_block=0
   rest_p2="/ "
   weapon_p2=" "



#keyboard logic and thread (to simultaneously press key):

#when we press key we do what is in this fonction (actually nothing)
def press_on(key):
    pass
#when we unpress the key we do what is in this fonction
def press_off(key):  
    global positionx_p1
    global positiony_p1
    global rest_p1
    global weapon_p1
    global player1_attack
    global player1_block

    global positiony_p2
    global positionx_p2 
    global rest_p2
    global weapon_p2
    global player2_attack
    global player2_block
    try:
        #player 1 keys set
        if key.char == 'd':
            if(positionx_p1<54):
                t=Timer(1/(2*movement_speed),move_right_p1)
                t.start()
        if key.char == 'a': #press a jump left (ascii 97)
            if(positionx_p1>3 and positiony_p1 >-1): # if we arrive at the left border we cannot jump left
                positiony_p1-=1
                positionx_p1-=3
                t=Timer(1/(2*movement_speed),jump1)
                t.start()
        if key.char == 'q': #press q go left
            if(positionx_p1>1): #if we arrive at the left border we cannot go left
                t=Timer(1/(2*movement_speed),move_left_p1)
                t.start()
        if key.char == 'e': #press e jump righ
            if(positionx_p1<54 and positiony_p1 >-1):
                positiony_p1-=1
                positionx_p1+=3
                t=Timer(1/(2*movement_speed),jump1)
                t.start()
        if key.char == 'z': # press z to attack
            if(player1_block==0):
                rest_p1=""
                weapon_p1="_"
                player1_attack=1
                t=Timer(attack_speed,switch_weapon_p1)
                t.start()
        if key.char == 's': # press s to block
            if(player1_attack==0):
                rest_p1=""
                weapon_p1="|"
                player1_block=1
                t=Timer(blocking_speed,switch_weapon_p1)
                t.start()

        #player 2 keys set
        if key.char == 'i': # i 105 jump left
            if(positionx_p2>3 and positiony_p2 >-1):
                positiony_p2-=1
                positionx_p2-=3
                t=Timer(1/(2*movement_speed),jump2)
                t.start()
        if key.char == 'm': #m 109 jump right
            if(positionx_p2<54 and positiony_p2 >-1):
                positiony_p2-=1
                positionx_p2+=3
                t=Timer(1/(2*movement_speed),jump2)
                t.start()
        if key.char == 'p': #p 112 block
            if(player2_attack==0):
                rest_p2=""
                weapon_p2="|"
                player2_block=1
                t=Timer(blocking_speed,switch_weapon_p2)
                t.start()
        if key.char == 'o': #o to attack
            if(player2_block==0):
                rest_p2=""
                weapon_p2="_"
                player2_attack=1
                t=Timer(attack_speed,switch_weapon_p2)
                t.start()
            
    except AttributeError:
        #some player 2 keys set
        if(key == Key.esc):
            return False
        if(key == Key.left):
            if(positionx_p2>1):
                t=Timer(1/(2*movement_speed),move_left_p2)
                t.start()
        if(key == Key.right):
            if(positionx_p2<55):
                t=Timer(1/(2*movement_speed),move_right_p2)
                t.start()
#key listener
def keyboard():
    with Listener(on_press=press_on ,on_release=press_off) as listener:
        listener.join()

#keyboard thread to simultaniously press key (player 1 can press key when player 2 press key too)
keyboard_thread=threading.Thread(target=keyboard)
keyboard_thread.start()

# GAME LOOP

while key != ESC:

    #display player
    clean()
    win.addstr(18, 1, current_scene) #ffscene display
    player1()
    player2()
    #fps display
    clock.tick(fps)
    win.addstr(0, 45, "FPS: " +str(round(clock.get_fps(),2)))

    win.addstr(1, 22, "Score : "+str(score[0])+" | "+str(score[1])) #score display
    


    key = win.getch()  #we wait for the next charactere

    if((positionx_p2 - positionx_p1) == 4):
        if(player1_attack==1 and player2_attack==1):
            positionx_p1=1
            positionx_p2=54
            time.sleep(0.25)
        if(player1_attack==1 and player2_block==0 and player2_attack==0):
            positionx_p1=1
            positionx_p2=54
            score[0]+=1
            time.sleep(0.25)
        if(player2_attack==1 and player1_block==0 and player1_attack==0):
            positionx_p1=1
            positionx_p2=54
            score[1]+=1
            time.sleep(0.25)
    

curses.endwin()
print(f"Final score = {score}"+ str(wall)+str(len(current_scene)))
