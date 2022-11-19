import turtle
janela = turtle.Screen()
janela.title("Ping Pong")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)    # stops the janela from updating
#   1st Paddle
raqueteUm = turtle.Turtle()
raqueteUm.speed(0)     # speed of animation, '0' for MAX
raqueteUm.color("white")
raqueteUm.shape("square")
raqueteUm.shapesize(largura=5, altura=1)  # 20*5 height
raqueteUm.penup()
raqueteUm.goto(-350, 0)    # (0, 0) is in middle
larguraUm = 5
#   2nd Paddle
raqueteDois = turtle.Turtle()
raqueteDois.speed(0)     # speed of animation, '0' for MAX
raqueteDois.color("white")
raqueteDois.shape("square")
raqueteDois.shapesize(largura=5, altura=1)
raqueteDois.penup()
raqueteDois.goto(350, 0)    # (0, 0) is in middle
larguraDois = 5
#   bola
bola = turtle.Turtle()
bola.speed(0)     # speed of animation, '0' for MAX
bola.color("white")
bola.shape("circle")
bola.penup()
bola.goto(0, 0)    # (0, 0) is in middle
bola.dx = 0.2     # bola moves by 2 pixels
bola.dy = -0.2
# for scoring
pontuacaoUm = 0
pontuacaoDois = 0
escritaDePontuacao = turtle.Turtle()
escritaDePontuacao.speed(0)
escritaDePontuacao.color("white")
escritaDePontuacao.penup()
escritaDePontuacao.hideturtle()
escritaDePontuacao.goto(0, 260)
escritaDePontuacao.write("Player One: 0        Player Two: 0", align="center", font=("Courier", 24, "normal"))
# movement of paddle
def raqueteUm_up():
    y = raqueteUm.ycor()   # coordinates
    y += 50
    raqueteUm.sety(y)
def raqueteUm_down():
    y = raqueteUm.ycor()   # coordinates
    y -= 50
    raqueteUm.sety(y)
def raqueteDois_up():
    y = raqueteDois.ycor()   # coordinates
    y += 50
    raqueteDois.sety(y)
def raqueteDois_down():
    y = raqueteDois.ycor()   # coordinates
    y -= 50
    raqueteDois.sety(y)
# Keyboard Events
janela.listen()
# Left one
janela.onkeypress(raqueteUm_up, 'w')
janela.onkeypress(raqueteUm_down, 's')
# right one
janela.onkeypress(raqueteDois_up, 'Up')
janela.onkeypress(raqueteDois_down, 'Down')
# main loop for the game to run
while True:
    janela.update()
    # bola Movement
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)
    # bola's Border checking
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1   # reversing direction
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1   # reversing direction
    if bola.xcor() > 390:   # past the paddle
        bola.goto(0, 0)
        bola.dx = -0.2
        if bola.dy > 0 : 
            bola.dy = 0.2
        else :
            bola.dy = -0.2
        pontuacaoUm += 1
        escritaDePontuacao.clear()
        escritaDePontuacao.write("Player One: {}           Player Two: {}".format(pontuacaoUm, pontuacaoDois), align="center",
                          font=("Courier", 24, "normal"))

        if (larguraUm != 1 and larguraDois != 1) :
            larguraUm -= 1
            larguraDois += 1
            raqueteUm.shapesize(largura=larguraUm, altura=1)
            raqueteDois.shapesize(largura=larguraDois, altura=1)
    if bola.xcor() < -390:   # past the paddle
        bola.goto(0, 0)
        bola.dx = 0.2
        if bola.dy > 0 : 
            bola.dy = 0.2
        else :
            bola.dy = -0.2
        pontuacaoDois += 1
        escritaDePontuacao.clear()
        escritaDePontuacao.write("Player One: {}           Player Two: {}".format(pontuacaoUm, pontuacaoDois), align="center",
                          font=("Courier", 24, "normal"))
        if (larguraUm != 1 and larguraDois != 1) :
            larguraDois -= 1
            larguraUm += 1
            raqueteDois.shapesize(largura=larguraDois, altura=1)
            raqueteUm.shapesize(largura=larguraUm, altura=1)
    # Collisions b/w bola & paddle
    if (340 < bola.xcor() < 350) and (raqueteDois.ycor() + 40 > bola.ycor() > raqueteDois.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1.05
        bola.dy *= 1.05
    if (-340 > bola.xcor() > -350) and (raqueteUm.ycor() + 40 > bola.ycor() > raqueteUm.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1.05
        bola.dy *= 1.05
