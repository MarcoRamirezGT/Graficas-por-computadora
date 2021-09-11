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

# Tele
rend.active_texture = Texture('textures/tele.bmp')
rend.normal_map = Texture('textures/tele_normal.bmp')

rend.active_shader = phong

rend.glLoadModel("models/televieja.obj",
                 translate=V3(3, -3, -9),
                 scale=V3(0.5, 0.5, 0.5),
                 rotate=V3(0, -67, 0))

# Coraje
rend.active_texture = Texture('textures/coraje.bmp')


rend.active_shader = toon

rend.glLoadModel("models/coraje.obj",
                 translate=V3(-4, -2, -7),
                 scale=V3(0.75, 0.75, 0.75),
                 rotate=V3(0, 67, 0))

# Fin
rend.active_texture = Texture('textures/finni1.bmp')


rend.active_shader = toon

rend.glLoadModel("models/finn1.obj",
                 translate=V3(-4, -3, -5),
                 scale=V3(0.5, 0.5, 0.5),
                 rotate=V3(0, 67, 0))

# Bellota
rend.active_texture = Texture('textures/bellota.bmp')
rend.active_shader = colors

rend.glLoadModel("models/bellota.obj",
                 translate=V3(-3, 3, -10),
                 scale=V3(0.25, 0.25, 0.25),
                 rotate=V3(45, 0, -45))

# Bellota
rend.active_texture = Texture('textures/bellota.bmp')
rend.active_shader = toon

rend.glLoadModel("models/bellota.obj",
                 translate=V3(-3, 5, -10),
                 scale=V3(0.25, 0.25, 0.25),
                 rotate=V3(45, 0, -45))


# Abuela
rend.active_texture = Texture('textures/abuela.bmp')
rend.active_shader = toon

rend.glLoadModel("models/abuela.obj",
                 translate=V3(7, -2, -11),
                 scale=V3(1, 1, 1),
                 rotate=V3(0, -67, 0))
# Bugs Bunny
rend.active_texture = Texture('textures/bunny.bmp')
rend.active_shader = toon

rend.glLoadModel("models/BugsBunny.obj",
                 translate=V3(-6, -2, -10),
                 scale=V3(3, 3, 3),
                 rotate=V3(0, -67, 0))
# Jerry
rend.active_texture = Texture('textures/jerry.bmp')
rend.active_shader = toon

rend.glLoadModel("models/jerry.obj",
                 translate=V3(7, -4, -8),
                 scale=V3(0.10, 0.1, 0.1),
                 rotate=V3(0, -45, 0))
# Claudio
rend.active_texture = Texture('textures/claudio.bmp')
rend.active_shader = toon

rend.glLoadModel("models/claudio.obj",
                 translate=V3(5, -2, -11),
                 scale=V3(1, 1, 1),
                 rotate=V3(0, -67, 0))


# Bellota mala
rend.active_texture = Texture('textures/bellota.bmp')
rend.active_shader = holographic

rend.glLoadModel("models/bellota.obj",
                 translate=V3(0, 3, -10),
                 scale=V3(0.25, 0.25, 0.25),
                 rotate=V3(0, 0, 135))

# Bellota mala
rend.active_texture = Texture('textures/bellota.bmp')
rend.active_shader = shader1

rend.glLoadModel("models/bellota.obj",
                 translate=V3(0, 5, -10),
                 scale=V3(0.25, 0.25, 0.25),
                 rotate=V3(0, 0, 135))


# Lucas
rend.active_texture = Texture('textures/lucas.bmp')
rend.active_shader = toon

rend.glLoadModel("models/lucas.obj",
                 translate=V3(-9, -2, -10),
                 scale=V3(3, 3, 3),
                 rotate=V3(0, 67, 0))
rend.glFinish("proyecto1.bmp")
