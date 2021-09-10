# Programa principal
from libraryGame import Renderer, V3
from obj import Texture
from shaders import *


width = 1920
height = 1080

rend = Renderer(width, height)

#rend.directional_light = V3(1, 0, 0)

rend.active_texture = Texture('textures/lucas.bmp')
rend.active_shader = phong

rend.glLoadModel("models/jerry.obj",
                 translate=V3(0, 0, -10),
                 scale=V3(1, 1, 1),
                 rotate=V3(0, 0, 0))
# rend.directional_light = V3(1, 1, 0)


rend.glFinish("output.bmp")
