from libraryGame import Renderer

width = 500
height = 500

rend = Renderer(width, height)

rend.glClearColor(0, 0.3, 0)
rend.glClear()

rend.glColor(0.2, 1, 1)
contX = 0
contY = 0
while contX < 20:
    contX += 1
    # Paredes de la pokebola
    for i in range(100):
        # Lado izquierdo
        rend.glPoint(100+contX, 200+i)
        rend.glPoint(-100+contX, 200+i)
        # Lado derecho
        # rend.glPoint(380+contX, 200+i)
    # Parte de arriba
    for i in range(50):
        # Lado izquierdo
        rend.glPoint(120+contX, 300+i)
        rend.glPoint(-120+contX, 300+i)
        # Lado derecho
        #rend.glPoint(360+contX, 300+i)
    # Tapa
    for i in range(40):
        # Lado izquierdo
        rend.glPoint(141+i, 349+contX)
        rend.glPoint(341+i, 349+contX)
        rend.glPoint(181+i, 369+contX)
        rend.glPoint(301+i, 369+contX)
        # rend.glPoint(340+i, 349+contX)
    for in in range(60):

    print(contX)


rend.glFinish("output.bmp")
