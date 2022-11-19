import turtle
import pygame

nomeDoUsuario = str(input("Insira seu nome: "))
emailDoUsuario = str(input("Insira seu email: "))

gui = pygame.image.load("assets/gui.png")
marcello = pygame.image.load("assets/marcello.png")

janela = turtle.Screen()
janela.title("Ping Pong")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)    
#   raquete um
raqueteUm = turtle.Turtle()
raqueteUm.speed(0)     # velocidade da animacao, '0' 
raqueteUm.color("white")
raqueteUm.shape("square")
raqueteUm.shapesize(stretch_wid=5, stretch_len=1)  # 20*5 altura
raqueteUm.penup()
raqueteUm.goto(-350, 0)    
larguraUm = 5
#    raquete dois
raqueteDois = turtle.Turtle()
raqueteDois.speed(0)     # velocidade da animacao, '0' 
raqueteDois.color("white")
raqueteDois.shape("square")
raqueteDois.shapesize(stretch_wid=5, stretch_len=1)
raqueteDois.penup()
raqueteDois.goto(350, 0)    
larguraDois = 5
bola = turtle.Turtle()
bola.speed(0)     
bola.color("white")
bola.shape("circle")
bola.penup()
bola.goto(0, 0)    
bola.dx = 0.2     
bola.dy = -0.2

pontuacaoUm = 0
pontuacaoDois = 0
escritaDePontuacao = turtle.Turtle()
escritaDePontuacao.speed(0)
escritaDePontuacao.color("white")
escritaDePontuacao.penup()
escritaDePontuacao.hideturtle()
escritaDePontuacao.goto(0, 250)
escritaDePontuacao.write("Jogador Um: 0        Jogador Dois: 0", align="center", font=("Courier", 24, "normal"))

def raqueteUm_up():
    y = raqueteUm.ycor()   
    y += 50
    raqueteUm.sety(y)
def raqueteUm_down():
    y = raqueteUm.ycor()   
    y -= 50
    raqueteUm.sety(y)
def raqueteDois_up():
    y = raqueteDois.ycor()  
    y += 50
    raqueteDois.sety(y)
def raqueteDois_down():
    y = raqueteDois.ycor()   
    y -= 50
    raqueteDois.sety(y)

janela.listen()
janela.onkeypress(raqueteUm_up, 'w')
janela.onkeypress(raqueteUm_down, 's')
janela.onkeypress(raqueteDois_up, 'Up')
janela.onkeypress(raqueteDois_down, 'Down')

while True:
    janela.update()
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1   
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1   
    if bola.xcor() > 390:   
        bola.goto(0, 0)
        bola.dx = -0.2
        if bola.dy > 0 : 
            bola.dy = 0.2
        else :
            bola.dy = -0.2
        pontuacaoUm += 1
        escritaDePontuacao.clear()
        escritaDePontuacao.write("Jogador Um: {}           Jogador Dois: {}".format(pontuacaoUm, pontuacaoDois), align="center",
                          font=("Courier", 24, "normal"))

        if (larguraUm != 1 and larguraDois != 1) :
            larguraUm -= 1
            larguraDois += 1
            raqueteUm.shapesize(stretch_wid=larguraUm, stretch_len=1)
            raqueteDois.shapesize(stretch_wid=larguraDois, stretch_len=1)
    if bola.xcor() < -390:   
        bola.goto(0, 0)
        bola.dx = 0.2
        if bola.dy > 0 : 
            bola.dy = 0.2
        else :
            bola.dy = -0.2
        pontuacaoDois += 1
        escritaDePontuacao.clear()
        escritaDePontuacao.write("Jogador Um: {}           Jogador Dois: {}".format(pontuacaoUm, pontuacaoDois), align="center",
                          font=("Courier", 24, "normal"))
        if (larguraUm != 1 and larguraDois != 1) :
            larguraDois -= 1
            larguraUm += 1
            raqueteDois.shapesize(stretch_wid=larguraDois, stretch_len=1)
            raqueteUm.shapesize(stretch_wid=larguraUm, stretch_len=1)
    if (340 < bola.xcor() < 350) and (raqueteDois.ycor() + 40 > bola.ycor() > raqueteDois.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1.05
        bola.dy *= 1.05
    if (-340 > bola.xcor() > -350) and (raqueteUm.ycor() + 40 > bola.ycor() > raqueteUm.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1.05
        bola.dy *= 1.05
    if pontuacaoDois and pontuacaoUm == 10:
        print("Parabens ao Ganhador!")
        break