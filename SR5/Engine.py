from libraryGame import Renderer, V3

from obj import Texture


width = 1920
height = 1080


rend = Renderer(width, height)
rend.glClearColor(1, 1, 1)
rend.glClear()

modelTexture = Texture("models/body2.bmp")


rend.glLoadModel("models/dragon.obj", modelTexture,
                 V3(1150, height/2, 0), V3(1, 1, 1))


rend.glFinish("dragonTexturizado.bmp")
