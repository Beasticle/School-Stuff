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
hitbox = 10

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
    self.speed(20)
    
  def right(self):
    self.forward(5)
    
  def left(self):
    self.backward(5)

Player_1 = Person(screen, 40, 25, 0, 'red')
Player_2 = Person(screen, 360, 25, 180, 'blue')

def setup():
  global Player_1, Player_2, listen
  
  listen = True
  
  screen.bgcolor('black')
  
  w = Turtle()
  w.ht()
  w.pu()
  w.color('white')
  w.width(5)
  w.speed()
  w.goto(5,10)
  w.pd()
  w.goto(395,10)
  w.goto(395,400)
  w.pu()
  w.goto(5,400)
  w.pd()
  w.goto(5,10)
  w.pu()
  
setup()

def play():
  global Player_1, Player_2, hitbox, listen
  
  def collide():
    return abs(Player_1.xcor()-Player_2.xcor()) <= hitbox #and (abs(Player_1.yc-Player_2.yc) <= hitbox)
  
  while True:
    collide()
    
    if listen == True:
      if keyboard.is_pressed('a') and collide == False:
        Player_1.right()
    
      
play()