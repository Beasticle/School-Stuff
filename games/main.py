from turtle import *
import keyboard
import random
import math
import time

screen = Screen()
screenMinX = 0
screenMinY = 0
screenMaxX = 400 
screenMaxY = 400
collisionbox = 10
hitbox = 15

screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)

class Person(Turtle):
  def __init__(self,screen,x,y, direction, color):
    Turtle.__init__(self)
    self.speed()
    self.ht()
    self.color(color)
    self.pu()
    self.goto(x,y)
    self.x0 = x
    self.y0 = y
    self.xc = self.xcor()
    self.yc = self.ycor()
    self.seth(direction)
    self.shape("turtle")
    self.screen = screen
    self.st()
    self.speed(2)
    self.health = 10
    self.strength = 1
    self.shield = False
    
  def right(self):
    self.forward(5)
    
  def left(self):
    self.backward(5)
    

def setup():
  global listen, w, Player_1, Player_2, gameend

  Player_1 = Person(screen, 40, 25, 0, 'red')
  Player_2 = Person(screen, 360, 25, 180, 'blue')
  gameend = False
  listen = True
  Player_1.health = 10
  Player_2.health = 10
  Player_1.shield = False
  Player_2.shield = False

  screen.bgcolor('black')
  
  w = Turtle()
  w.ht()
  w.pu()
  w.color('white')
  w.width(5)
  w.speed(200000000)
  w.goto(5,10)
  w.pd()
  w.goto(395,10)
  w.goto(395,400)
  w.pu()
  w.goto(5,400)
  w.pd()
  w.goto(5,10)
  w.pu()
  w.goto(200,200)
  
setup()

def collide():
    return abs(Player_1.xcor()-Player_2.xcor()) <= collisionbox

def attack():
  if keyboard.is_pressed('f') and gameend == False:
    if Player_2.xcor()-Player_1.xcor() <= hitbox:
      Player_2.health = Player_2.health - Player_1.strength
      print("Player 1 attacked Player 2")
      print(Player_2.health)
      time.sleep(.1)
  if keyboard.is_pressed('m') and gameend == False:
    if Player_2.xcor()-Player_1.xcor() <= hitbox:
      Player_1.health = Player_1.health - Player_2.strength
      print("Player 2 attacked Player 1")
      print(Player_1.health)
      time.sleep(.1)
def win():
  global gameend, w
  if Player_1.health <= 0:
    w.goto(200,200)
    w.write("Player 2 is the winner!")
    gameend = True
  if Player_2.health <= 0:
    w.goto(200,200)
    w.write("Player 1 is the winner!")   
    gameend = True
  if keyboard.is_pressed('r'):
      screen.clear()
      setup()
      play()
      print('Game has reset')

def play():
  global Player_1, Player_2, collisionbox, hitbox, listen, w, attack, win, collide, gameend
  listen = True  
  
  while True:
    collide()
    attack()
    win()
    
    if collide() == False and gameend == False:
      if keyboard.is_pressed('a'):
        if Player_1.xcor() < 5:
          Player_1.forward(5)
        else:
          Player_1.left()
      if keyboard.is_pressed('d'):
        if Player_1.xcor() > 395:
          Player_1.backward(5)
        else:
          Player_1.right()
      if keyboard.is_pressed('left'):
        if Player_2.xcor() < 5:
          Player_2.backward(5)
        else:
          Player_2.right()
      if keyboard.is_pressed('right'):
        if Player_2.xcor() > 395:
          Player_2.forward(5)
        else:
          Player_2.left()
    elif gameend == False:
      if keyboard.is_pressed('d') and keyboard.is_pressed('left'):
        if keyboard.is_pressed('a'):
          Player_1.back(5)
        if keyboard.is_pressed('right'):
          Player_2.back(5)
      else:
        Player_1.back(10)
        Player_2.back(10)
     
play()