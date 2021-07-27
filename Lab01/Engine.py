from libraryGame import Renderer, V2

width = 500
height = 500


rend = Renderer(width, height)
Poligono1 = [(V2(165, 380)), (V2(185, 360)), (V2(180, 330)), (V2(207, 345)), (V2(233, 330)),
             (V2(230, 360)), (V2(250, 380)), (V2(220, 385)), (V2(205, 410)), (V2(193, 383))]


rend.glLine(Poligono1[0], Poligono1[1])
rend.glLine(Poligono1[1], Poligono1[2])
rend.glLine(Poligono1[2], Poligono1[3])
rend.glLine(Poligono1[3], Poligono1[4])
rend.glLine(Poligono1[4], Poligono1[5])
rend.glLine(Poligono1[5], Poligono1[6])
rend.glLine(Poligono1[6], Poligono1[7])
rend.glLine(Poligono1[7], Poligono1[8])
rend.glLine(Poligono1[8], Poligono1[9])
rend.glLine(Poligono1[9], Poligono1[0])


Poligono2 = [(V2(321, 335)), (V2(288, 286)), (V2(339, 251)), (V2(374, 302))]

rend.glLine(Poligono2[0], Poligono2[1])
rend.glLine(Poligono2[1], Poligono2[2])
rend.glLine(Poligono2[2], Poligono2[3])
rend.glLine(Poligono2[3], Poligono2[0])

Poligono3 = [
    (377, 249)(411, 197)(436, 249)]


# for x in range(165):
# rend.glPoint((x*x+1)//2, (x*x+1)//2)

rend.glFinish("Lab01.bmp")
