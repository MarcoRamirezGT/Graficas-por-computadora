# Programa principal
from libraryGame import Renderer, V3
from obj import Texture
from shaders import *


width = 1920
height = 1080

rend = Renderer(width, height)

rend.directional_light = V3(0, 0, -1)
rend.background = Texture('textures/fondo.bmp')

rend.glClearBackground()


rend.active_texture = Texture('textures/tele.bmp')
rend.normal_map = Texture('textures/tele_normal.bmp')

rend.active_shader = phong

rend.glLoadModel("models/televieja.obj",
                 translate=V3(6, -3, -10),
                 scale=V3(0.25, 0.25, 0.25),
                 rotate=V3(0, -135, 0))
# rend.directional_light = V3(1, 1, 0)


rend.glFinish("output.bmp")
