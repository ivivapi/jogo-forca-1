import turtle          # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Jogo Da Forca")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(10)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-250,-200)
tartaruga.pendown()
tartaruga.color("blue")

dist = 120

tartaruga.forward(120) #forca
tartaruga.backward(60)
tartaruga.left(90)
tartaruga.forward(400)
tartaruga.left(270)
tartaruga.forward(150)
tartaruga.right(90)
tartaruga.forward(70)
tartaruga.penup()   # cabeça
tartaruga.setpos(-80,90)
tartaruga.pendown()
tartaruga.circle(40)
tartaruga.penup()
tartaruga.setpos(-40,50)
tartaruga.pendown()   # corpo
tartaruga.forward(150)
tartaruga.backward(125)   # braço 1
tartaruga.left(60)
tartaruga.forward(70)
tartaruga.backward(70)
tartaruga.right(125)    # braço2
tartaruga.forward(70)
tartaruga.backward(70) 
tartaruga.left(65)    # perna1
tartaruga.forward(125)
tartaruga.left(35)
tartaruga.forward(100)
tartaruga.backward(100)
tartaruga.right(75)   # perna2
tartaruga.forward(100)
