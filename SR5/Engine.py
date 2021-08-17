from libraryGame import Renderer, V3, _color

from obj import Texture


width = 1920
height = 1080

rend = Renderer(width, height)

modelTexture = Texture("models/model.bmp")

modelPosition = V3(0, 0, -10)

rend.glLookAt(modelPosition, V3(0, 8, 0))

rend.glLoadModel("models/model.obj",
                 modelTexture,
                 translate=modelPosition,
                 scale=V3(3, 3, 3),
                 rotate=V3(0, 0, 0))


rend.glFinish("high.bmp")
