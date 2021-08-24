# Programa principal
from libraryGame import Renderer, V3, _color
from obj import Texture
from shaders import *

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.directional_light = V3(1, 0, 0)

rend.active_texture = Texture('models/model.bmp')
rend.active_shader = toon

rend.glLoadModel("models/Madara_Uchiha.obj",
                 translate=V3(0, 0, -10),
                 scale=V3(0.001, 0.001, 0.001),
                 rotate=V3(0, 0, 0))

rend.glFinish("output.bmp")
