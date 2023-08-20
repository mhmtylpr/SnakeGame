import turtle
from time import sleep
import random
import winsound

#sabit değerler hazırlandı

SCORE = 0
SPEED = 0.15
FONT = ("Arial", 17 , "normal")
TAIL = list()

#screen oluşturuldu

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("Black")
screen.setup(width=600, height=600)
screen.tracer(0)

#scor ekranı oluşturuldu

score_boar = turtle.Turtle()
score_boar.hideturtle()
score_boar.penup()
score_boar.goto(x=0, y=600/2*0.9)
score_boar.color("orange")
score_boar.write(arg="Score: 0", align="center", font=FONT)

#yılanın kafası oluşturuldu

snake = turtle.Turtle()
snake.shape("circle")
snake.color("blue")
snake.penup()
snake.shapesize(1)
snake.goto(0, 100)
snake.dicection = "stop"

#yılanın hareket sistemi oluşturuldu

def move():
    if snake.dicection == "w":
        y =snake.ycor()
        snake.sety(y+20)
    if snake.dicection == "s":
        y =snake.ycor()
        snake.sety(y-20)
    if snake.dicection == "a":
        x =snake.xcor()
        snake.setx(x-20)
    if snake.dicection == "d":
        x =snake.xcor()
        snake.setx(x+20)

#yılanın gittiği yönün tersine gitmesi engellendi

class moveDirection():
    def goUp(self):
        if snake.dicection != "w":
            snake.dicection = "s"
    def goDown(self):
        if snake.dicection != "s":
            snake.dicection = "w"
    def goRight(self):
        if snake.dicection != "a":
            snake.dicection = "d"
    def goLeft(self):
        if snake.dicection != "d":
            snake.dicection = "a"

#yılanın yemeği tasarlandı

eatTurtle = turtle.Turtle()
eatTurtle.color("red")
eatTurtle.shape("turtle")
eatTurtle.penup()
eatTurtle.shapesize(0.8,0.8)
eatTurtle.goto(35,40)

#tuş kombinasyonları oluşturuldu

screen.listen()
screen.onkey(moveDirection().goUp,"s")
screen.onkey(moveDirection().goDown,"w")
screen.onkey(moveDirection().goLeft,"a")
screen.onkey(moveDirection().goRight,"d")
screen.onkey(moveDirection().goUp,"S")
screen.onkey(moveDirection().goDown,"W")
screen.onkey(moveDirection().goLeft,"A")
screen.onkey(moveDirection().goRight,"D")

#sürekli çalışması istenilen istemler döngüye konuldu

while True:

    screen.update()

    #oyunda kaybedince oluşacak game over mesajı için turtle oluşturuldu

    game = turtle.Turtle()
    game.hideturtle()

    #kenara çarpması durumunda game over mesajı verildi

    if snake.xcor() == 300 or snake.xcor() == -300 or snake.ycor() == 300 or snake.xcor()==-300:

        # kaybetme durumunda ses eklendi

        winsound.PlaySound('game-over.wav', winsound.SND_ASYNC)
        snake.goto(0, 100)
        snake.write(arg="Game Over\nReturn to 'SPACE' \n", align="center", font=("Arial", 25, "bold"))
        game.clear()
        snake.dicection = "stop"

        #yılanın kuyruğu ana ekran dan uzaklaştırldı

        for i in TAIL:
            i.goto(1000,1000)

        TAIL.clear()

    #yılanın kendi kuyruğunu ısırması durumunda oluşsacak mağlubiyet durumu eklendi

    for i in TAIL:

        if snake.distance(i) < 20:

            #kaybetme durumunda ses eklendi
            winsound.PlaySound('game-over.wav', winsound.SND_ASYNC)
            snake.goto(0, 100)
            snake.write(arg="You bit Yourself\nReturn to 'SPACE' \n", align="center", font=("Arial", 25, "bold"))
            game.clear()
            snake.dicection = "stop"

            for i in TAIL:
                i.goto(1000, 1000)
            TAIL.clear()

    #Oyunu yeniden başlatma sistemi oluşturuldu

    def restart ():
        snake.clear()
        snake.goto(0,100)
    screen.listen()
    screen.onkey(restart,"space")

    #yemeğin yenmesi durumunda skor ve kuyruktaki artış hazrlandı

    if eatTurtle.distance(snake)<20:
        winsound.PlaySound('snake.wav', winsound.SND_ASYNC)
        x = random.randint(1, 280)
        y = random.randint(1, 280)
        eatTurtle.goto(x, y)
        SCORE  += 1
        score_boar.clear()
        score_boar.write(arg="Score: {}".format(SCORE), align="center", font=FONT)

        #kuruk turtle oluşturldu
        new_tail = turtle.Turtle()
        new_tail.penup()
        new_tail.shape("circle")
        new_tail.color("green")
        TAIL.append(new_tail)

    #oluşturulmuş olan kuyruğun ekleme sistemi oluşturuldu

    for i in range(len(TAIL)-1,0,-1):
        x = TAIL[i-1].xcor()
        y = TAIL[i - 1].ycor()
        TAIL[i].goto(x,y)
    if len(TAIL)>0:

        x = snake.xcor()
        y = snake.ycor()
        TAIL[0].goto(x,y)

    move()
    sleep(SPEED)



