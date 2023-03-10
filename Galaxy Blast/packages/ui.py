from turtle import Turtle

class UI():

    def __init__(self, highscore):
        self.score = Turtle()
        self.score.score = 0
        self.score.penup()
        self.score.pencolor('white')
        self.score.hideturtle()
        self.score.goto(-5, 270)
        self.high_score = Turtle()
        self.high_score.score = highscore
        self.high_score.penup()
        self.high_score.pencolor('white')
        self.high_score.hideturtle()
        self.high_score.goto(-270, 270)
        self.hp = Turtle()
        self.hp.hp = 3
        self.hp.penup()
        self.hp.pencolor('white')
        self.hp.hideturtle()
        self.hp.goto(240, 270)

    def draw(self):
        self.score.clear()
        self.high_score.clear()
        self.hp.clear()
        self.score.write(f'Score: {self.score.score}', move = False, font = ('arial', 12, 'bold'))
        self.high_score.write(f' High-Score: {self.high_score.score}', move = False, font = ('arial', 12, 'bold'))
        self.hp.write(f'HP: {self.hp.hp}', move = False, font = ('arial', 12, 'bold'))

    def undraw(self):
        self.score.clear()
        self.high_score.clear()
        self.hp.clear()


class SplashScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('imgs/splashscreen.gif')

    def undraw(self):
        self.hideturtle()

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def gameover(self):
        self.shape('imgs/gameover.gif')
        self.showturtle()

    def gameoverhighscore(self):
        self.shape('imgs/gameoverhighscore.gif')
        self.showturtle()

    def hide(self):
        self.hideturtle()

