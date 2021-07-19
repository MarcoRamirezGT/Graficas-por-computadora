from libraryGame import Renderer, V2
width = 500
height = 500

rend = Renderer(width, height)


rend.glLine(V2(height//2, width//2), V2(200, 220))
rend.glLine(V2(height//2, width//2), V2(300, 220))
rend.glLine(V2(200, 220), V2(210, 160))
rend.glLine(V2(300, 220), V2(290, 160))
rend.glLine(V2(290, 160), V2(210, 160))


rend.glLine(V2(height//2, width//2), V2(210, 160))
rend.glLine(V2(height//2, width//2), V2(290, 160))
rend.glLine(V2(290, 160), V2(200, 220))
rend.glLine(V2(210, 160), V2(300, 220))
rend.glLine(V2(200, 220), V2(300, 220))


rend.glLine(V2(190, 150), V2(310, 150))
rend.glLine(V2(190, 150), V2(190, 260))
rend.glLine(V2(190, 260), V2(310, 260))
rend.glLine(V2(310, 260), V2(310, 150))

rend.glLine(V2(0, height-10), V2(10, height))


for y in range(width):
    datX = 0
    datY = height-(y*10)
    datX2 = y*10
    datY2 = height
    if datX2 < 440 or datX2 > 650:
        rend.glLine(V2(datX, datY), V2(datX2, datY2))


for x in range(width):
    datx = 0*x
    daty = 10*x

    if daty < 350 or daty > 560:
        print(datx, daty)
        rend.glLine(V2(datx, daty), V2(daty, datx))


rend.glFinish("Lineas.bmp")
