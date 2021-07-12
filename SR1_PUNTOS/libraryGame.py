import struct


def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    # 2 bytes
    return struct.pack('=h', w)


def dword(d):
    # 4 bytes
    return struct.pack('=l', d)


def color(r, g, b):
    # Acepta valores de 0 a 1
    return bytes([int(b*255), int(g*255), int(r*255)])


BLACK = color(0, 0, 0)
WHITE = color(1, 1, 1)


class Renderer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def function(self):
        self.width
