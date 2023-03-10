# ### To-Do ###
# - Find bug that sometimes crashes game


from packages import *
from turtle import *
from time import sleep


save = open('data/highscore.txt', mode = 'r')
highscore = int(save.read())
save.close()


menu = 'start'


win = Screen()
win.setup(600,600)
win.title('GALAXY BALST')
win.fav
win.bgpic("imgs/background.gif")
win.addshape('sprites/spaceship.gif')
win.addshape('sprites/asteroid.gif')
win.addshape('sprites/laser.gif')
win.addshape('imgs/splashscreen.gif')
win.addshape('imgs/gameover.gif')
win.addshape('imgs/gameoverhighscore.gif')
win.tracer(0)


user = Player()
roids = AsteroidMaker()
interface = UI(highscore)
interface.draw()
splash = SplashScreen()
gameovr = GameOver()


def start_game():
    global menu
    menu = 'play'


win.onkeypress(user.move_left, 'a')
win.onkeypress(user.move_right, 'd')
win.onkeypress(user.shoot, "space")
win.onkeypress(start_game, 'Control_L')
win.listen()


while True:

    while menu == 'start':
        win.update()
        sleep(0.025)

    splash.undraw()
    user.restart()
    roids.restart()

    while menu == 'play':

        # Object Movement
        roids.move_asteroids()
        user.bullet_move()

        # Collisions
        for laser in user.bullets:
            for asteroid in roids.asteroids:
                if laser.xcor() >= asteroid.xcor() - 30 and laser.xcor() <= asteroid.xcor() + 30:
                    if laser.ycor() >= asteroid.ycor() - 30:
                        asteroid.clear()
                        asteroid.hideturtle()
                        roids.asteroids.remove(asteroid)
                        laser.clear()
                        laser.hideturtle()
                        user.bullets.remove(laser)
                        interface.score.score += 1
                        interface.draw()
                        if interface.score.score % 10 == 0:
                            roids.dy = roids.dy * 1.1
        for asteroid in roids.asteroids:
            if asteroid.ycor() <= -330:
                asteroid.clear()
                asteroid.hideturtle()
                roids.asteroids.remove(asteroid)
                interface.hp.hp -= 1
                interface.draw()
        
        # State Checking
        if interface.hp.hp <= 0:
            menu = 'gameover'

        # Asteroid Handling
        if len(roids.asteroids) < roids.ast_max:
            roids.spawn()

        # Window Refresh    
        win.update()
        sleep(0.025)

    while menu == 'gameover':
        if interface.score.score > interface.high_score.score:
            save = open('data/highscore.txt', mode = 'w')
            save.write(str(interface.score.score))
            save.close()
            interface.high_score.score = interface.score.score
            interface.draw()
            gameovr.gameoverhighscore()
            menu = 'wait'
        else:
            gameovr.gameover()
            menu = 'wait'
        interface.score.score = 0
        interface.hp.hp = 3

    while menu == 'wait':
        win.update()
        sleep(0.025)
        
    gameovr.hide()