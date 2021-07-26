from libraryGame import Renderer, V2, color


width = 1920
height = 1080

rend = Renderer(width, height)

rend.glLoadModel("models/dragon.obj", V2(1150, height/2), V2(1, 1))


rend.glFinish("dragon.bmp")
