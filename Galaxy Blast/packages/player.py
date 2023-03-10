from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.bullets = []
        self.penup()
        self.shape('sprites/spaceship.gif')
        self.sety(-240)
    
    def move_left(self):
        self.setx(self.xcor() - 50)
        if self.xcor() <= -280:
            self.setx(-280)

    def move_right(self):
        self.setx(self.xcor() + 50)
        if self.xcor() >= 280:
            self.setx(280)

    def shoot(self):
        bullet = Turtle()
        bullet.penup()
        bullet.shape('sprites/laser.gif')
        bullet.setx(self.xcor())
        bullet.sety(self.ycor())
        bullet.dy = 10
        self.bullets.append(bullet)

    def bullet_move(self):
        for bullets in self.bullets:
            bullets.sety(bullets.ycor() + 20)
            if bullets.ycor() >= 330:
                bullets.clear()
                bullets.hideturtle()
                self.bullets.remove(bullets)

    def restart(self):
        for bullets in self.bullets:
            bullets.hideturtle()
        self.bullets = []
        self.setx(0)
        