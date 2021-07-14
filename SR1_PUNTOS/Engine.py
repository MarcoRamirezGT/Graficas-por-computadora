
from libraryGame import Renderer

width = 500
height = 500

rend = Renderer(width, height)

rend.glClearColor(1, 1, 1)
rend.glClear()


contX = 0
contY = 0

while contX < 20:

    rend.glColor(0, 0, 0)
    contX += 1
    # Paredes de la pokebola
    for i in range(100):
        # Izquierda
        rend.glPoint(100+contX, 200+i)

        # Derecha
        rend.glPoint(-100+contX, 200+i)

    # Parte de arriba
    for i in range(50):
        # ARRIBA IZQUIERA

        rend.glPoint(120+contX, 300+i)
        # Derecha
        rend.glPoint(-120+contX, 300+i)
        # ABAJO izquierda
        rend.glPoint(120+contX, -350+i)
        # Abajo derecha
        rend.glPoint(-120+contX, -350+i)

    # Tapa
    for i in range(40):
        # Arriba
        # Izquierda
        rend.glPoint(141+i, 349+contX)
        rend.glPoint(341+i, 349+contX)
        # Derecha
        rend.glPoint(181+i, 369+contX)
        rend.glPoint(301+i, 369+contX)
        # Abajo
        rend.glPoint(141+i, -371+contX)
        rend.glPoint(341+i, -371+contX)
        rend.glPoint(181+i, -391+contX)
        rend.glPoint(301+i, -391+contX)
    for i in range(80):
        # Arriba
        rend.glPoint(221+i, 389+contX)
        # Abajo
        rend.glPoint(221+i, -411+contX)
    for i in range(30):
        # Elementos dentro
        rend.glPoint(120+contX, 240+i)
        rend.glPoint(-120+contX, 240+i)
    for i in range(40):
        rend.glPoint(181+i, 199+contX)
        rend.glPoint(141+i, 219+contX)

        rend.glPoint(341+i, 219+contX)

        # Abajo

    for i in range(60):
        rend.glPoint(181+i, 199+contX)
        rend.glPoint(281+i, 199+contX)
    for i in range(30):
        # Elementos dentro
        rend.glPoint(220+contX, 220+i)
        rend.glPoint(-220+contX, 220+i)
    for i in range(40):
        rend.glPoint(241+i, 179+contX)
        rend.glPoint(241+i, 249+contX)

    print(contX)
    rend.glViewport(100, 100, 400, 400)

rend.glFinish("output.bmp")
