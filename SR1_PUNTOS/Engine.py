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
        # Lado izquierdo
        rend.glPoint(100+contX, 200+i)

        rend.glPoint(-100+contX, 200+i)

    # Parte de arriba
    for i in range(50):

        rend.glPoint(120+contX, 300+i)
        rend.glPoint(-120+contX, 300+i)
        rend.glPoint(120+contX, -350+i)
        rend.glPoint(-120+contX, -350+i)

    # Tapa
    for i in range(40):

        rend.glPoint(141+i, 349+contX)
        rend.glPoint(341+i, 349+contX)
        rend.glPoint(181+i, 369+contX)
        rend.glPoint(301+i, 369+contX)

        rend.glPoint(141+i, -371+contX)
        rend.glPoint(341+i, -371+contX)
        rend.glPoint(181+i, -391+contX)
        rend.glPoint(301+i, -391+contX)
    for i in range(80):
        rend.glPoint(221+i, 389+contX)
        rend.glPoint(221+i, -411+contX)

    print(contX)
rend.glColor(0.8, 0.5, 0.8)
rend.glPoint(50, 50)

rend.glFinish("output.bmp")
