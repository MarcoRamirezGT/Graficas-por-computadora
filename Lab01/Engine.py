from libraryGame import Renderer, V2, color
import sys
import random

width = 1920
height = 1080

rend = Renderer(width, height)

# Estrella
rend.glTriangle(V2(205, 410),  V2(193, 383), V2(220, 385), color(0, 1, 0))

rend.glTriangle(V2(165, 380), V2(193, 383),  V2(185, 360),  color(0, 1, 0))
rend.glTriangle(V2(207, 345), V2(180, 330),  V2(185, 360),  color(0, 1, 0))
rend.glTriangle(V2(207, 345), V2(233, 330),  V2(230, 360),  color(0, 1, 0))
rend.glTriangle(V2(230, 360), V2(250, 380),  V2(220, 385),  color(0, 1, 0))
rend.glTriangle(V2(208, 366), V2(185, 360),  V2(207, 345),  color(0, 1, 0))
rend.glTriangle(V2(208, 366), V2(193, 383),  V2(220, 385),  color(0, 1, 0))
rend.glTriangle(V2(208, 366), V2(185, 360),  V2(205, 411),  color(0, 1, 0))
rend.glTriangle(V2(208, 366), V2(220, 385),  V2(230, 360),  color(0, 1, 0))
rend.glTriangle(V2(208, 366), V2(230, 360),  V2(207, 345),  color(0, 1, 0))

# Cuadrado
rend.glTriangle(V2(321, 335), V2(374, 302),  V2(288, 286),  color(1, 0, 0))
rend.glTriangle(V2(339, 251), V2(374, 302),  V2(288, 286),  color(1, 0, 0))

# Triangulo
rend.glTriangle(V2(377, 249), V2(411, 197), V2(436, 249),  color(0, 0, 1))


# Poligono4 = [(V2(413, 177)), (V2(448, 159)), (V2(502, 88)), (V2(553, 53)), (V2(535, 36)), (V2(676, 37)), (V2(660, 52)),
#              (V2(750, 145)), (V2(761, 179)), (V2(672, 192)), (V2(659, 214)
#                                                               ), (V2(615, 214)), (V2(632, 230)), (V2(580, 230)),
#              (V2(597, 215)), (V2(552, 214)), (V2(517, 144)), (V2(466, 180))
#              ]

# for x in range(len(Poligono4)):
#     rend.glLine(Poligono4[x], Poligono4[(x+1) % len(Poligono4)])

# Poligono5 = [(V2(682, 175)), (V2(708, 120)), (V2(735, 148)), (V2(739, 170))]


# for x in range(len(Poligono5)):
#     rend.glLine(Poligono5[x], Poligono5[(x+1) % len(Poligono5)])


rend.glFinish("lab01.bmp")
