import pgzrun
import random
WIDTH=800
HEIGHT=600
steve=Actor("steve")
zombie=Actor("zombie")
mom=Actor("mom")
score=0

def draw():
    screen.fill((125, 179, 255))
    steve.draw()
    zombie.draw()
    screen.draw.text("score : "+ str (score), topleft=(0,0), color=(245, 44, 104),fontsize=50)
    if score>=30:
        screen.fill((0, 0, 0))
        mom.draw()
        screen.draw.text("STOP GAMING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",center=(600,400),color=(245, 44, 104),fontsize=70)
def move():
    steve.x=random.randint(0,800)
    steve.y=random.randint(0,600)
    zombie.x=random.randint(0,800)
    zombie.y=random.randint(0,600)
move()

def update():
    global score
    if keyboard.up:
        zombie.y=zombie.y-10
    if keyboard.down:
        zombie. y=zombie.y+10
    if keyboard. right:
        zombie. x=zombie. x+10
    if keyboard. left:
        zombie. x=zombie. x-10
    if zombie.colliderect(steve):
        score=score+1
        move()
    
    





































pgzrun.go()
    
