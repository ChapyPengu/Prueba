import turtle 

juego = turtle.Screen()
juego.title("Pong by Chapy Pengu")
juego.bgcolor("black")
juego.setup(width = 800, height = 600)
juego.tracer(0)

jugador_1 = turtle.Turtle()
jugador_1.speed(0)
jugador_1.shape("square")
jugador_1.color("white")
jugador_1.penup()
jugador_1.goto(-350, 0)
jugador_1.shapesize(stretch_wid = 5, stretch_len = 1)

jugador_2 = turtle.Turtle()
jugador_2.speed(0)
jugador_2.shape("square")
jugador_2.color("white")
jugador_2.penup()
jugador_2.goto(350, 0)
jugador_2.shapesize(stretch_wid = 5, stretch_len = 1)

pelota_1 = turtle.Turtle()
pelota_1.speed(0)
pelota_1.shape("circle")
pelota_1.color("white")
pelota_1.penup()
pelota_1.goto(0, 0)
pelota_1.shapesize(stretch_wid = 1, stretch_len = 1)
pelota_1.dx = 0.5
pelota_1.dy = 0.5

cancha = turtle.Turtle()
cancha.speed(0)
cancha.shape("square")
cancha.color("white")
cancha.goto(0, -280)
cancha.goto(0, 290)
cancha.goto(380, 290)
cancha.goto(380, -280)
cancha.goto(-380, -280)
cancha.goto(-380, 290)
cancha.goto(380, 290)
cancha.goto(400, 400)

puntos_jugador_1 = 0
puntos_jugador_2 = 0
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.hideturtle()
marcador.goto(0, 250)
marcador.write(f"JugadorA: {puntos_jugador_1}              JugadorB: {puntos_jugador_2}", align = "center", font = ("Courier", 20))

def jugador_1_movimiento_superior():
    y = jugador_1.ycor()
    if y < 230:    
        y += 20
    jugador_1.sety(y)
def jugador_1_movimiento_inferior():
    y = jugador_1.ycor()
    if y > -210:    
        y -= 20
    jugador_1.sety(y)
def jugador_2_movimiento_superior():
    y = jugador_2.ycor()
    if y < 230:
        y += 20
    jugador_2.sety(y)
def jugador_2_movimiento_inferior():
    y = jugador_2.ycor()
    if y > -210:
        y -= 20
    jugador_2.sety(y)

juego.listen()
juego.onkeypress(jugador_1_movimiento_superior, "w")
juego.onkeypress(jugador_1_movimiento_inferior, "s")
juego.onkeypress(jugador_2_movimiento_superior, "i")
juego.onkeypress(jugador_2_movimiento_inferior, "k")


while True:
    juego.update()

    pelota_1.setx(pelota_1.xcor() + pelota_1.dx)
    pelota_1.sety(pelota_1.ycor() + pelota_1.dy)

    if pelota_1.ycor() > 280:
        pelota_1.dy *= -1
    if pelota_1.ycor() < -280:
        pelota_1.dy *= -1
    if pelota_1.xcor() > 380:
        pelota_1.goto(0, 0)
        pelota_1.dx *= -1
        puntos_jugador_1 += 1
        marcador.clear()
        marcador.write(f"JugadorA: {puntos_jugador_1}              JugadorB: {puntos_jugador_2}", align = "center", font = ("Courier", 20)) 
    if pelota_1.xcor() < -380:
        pelota_1.goto(0, 0)
        pelota_1.dx *= -1
        puntos_jugador_2 += 1
        marcador.clear()
        marcador.write(f"JugadorA: {puntos_jugador_1}              JugadorB: {puntos_jugador_2}", align = "center", font = ("Courier", 20))

    if ((pelota_1.xcor() > 340 and pelota_1.xcor() < 350) 
        and (pelota_1.ycor() < jugador_2.ycor() + 50) 
        and (pelota_1.ycor() > jugador_2.ycor() - 50)):  
        pelota_1.dx *= -1
    if (pelota_1.xcor() < -340 and pelota_1.xcor() > -350) and (pelota_1.ycor() < jugador_1.ycor() + 50) and (pelota_1.ycor() > jugador_1.ycor() - 50):
        pelota_1.dx *= -1
