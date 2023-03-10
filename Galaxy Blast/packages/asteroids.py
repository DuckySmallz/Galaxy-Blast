from turtle import Turtle
from random import randint


class AsteroidMaker():
    
    def __init__(self):
        self.y = 330
        self.dy = 2
        self.ast_max = 6
        self.asteroids = []

    def spawn(self):
        asteroid = Turtle()
        asteroid.penup()
        asteroid.sety(self.y + randint(10, 600))
        asteroid.setx(randint(-270, 270))
        asteroid.shape('sprites/asteroid.gif')
        asteroid.dy = self.dy
        self.asteroids.append(asteroid)

    def move_asteroids(self):
        for asteroid in self.asteroids:
            asteroid.sety(asteroid.ycor() - asteroid.dy)

    def restart(self):
        self.dy = 2
        for asteroids in self.asteroids:
            asteroids.hideturtle()
        self.asteroids = []
            
    