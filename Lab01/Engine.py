from libraryGame import Renderer, V2
import sys
import random

width = 1920
height = 1080

rend = Renderer(width, height)
Poligono1 = [(V2(165, 380)), (V2(185, 360)), (V2(180, 330)), (V2(207, 345)), (V2(233, 330)),
             (V2(230, 360)), (V2(250, 380)), (V2(220, 385)), (V2(205, 410)), (V2(193, 383))]

for x in range(len(Poligono1)):
    print(x)
    print(Poligono1[x])

    rend.glLine(Poligono1[x], Poligono1[(x+1) % len(Poligono1)])
    for y in range(3):
        rend.glLine((V2(165+y, 380-y)), (V2(185+y, 360+y)))


Poligono2 = [(V2(321, 335)), (V2(288, 286)), (V2(339, 251)), (V2(374, 302))]

for x in range(len(Poligono2)):
    rend.glLine(Poligono2[x], Poligono2[(x+1) % len(Poligono2)])

Poligono3 = [(V2(377, 249)), (V2(411, 197)), (V2(436, 249))]
for x in range(len(Poligono3)):
    rend.glLine(Poligono3[x], Poligono3[(x+1) % len(Poligono3)])


Poligono4 = [(V2(413, 177)), (V2(448, 159)), (V2(502, 88)), (V2(553, 53)), (V2(535, 36)), (V2(676, 37)), (V2(660, 52)),
             (V2(750, 145)), (V2(761, 179)), (V2(672, 192)), (V2(659, 214)
                                                              ), (V2(615, 214)), (V2(632, 230)), (V2(580, 230)),
             (V2(597, 215)), (V2(552, 214)), (V2(517, 144)), (V2(466, 180))
             ]

for x in range(len(Poligono4)):
    rend.glLine(Poligono4[x], Poligono4[(x+1) % len(Poligono4)])

Poligono5 = [(V2(682, 175)), (V2(708, 120)), (V2(735, 148)), (V2(739, 170))]


for x in range(len(Poligono5)):
    rend.glLine(Poligono5[x], Poligono5[(x+1) % len(Poligono5)])


rend.glFinish("Lab01.bmp")
