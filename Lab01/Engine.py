from libraryGame import Renderer, V2, color


width = 900

height = 500

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

# Taza
a = V2(413, 177)
b = V2(448, 159)
c = V2(502, 88)
d = V2(553, 53)
e = V2(535, 36)
f = V2(676, 37)
g = V2(660, 52)
h = V2(750, 145)
i = V2(761, 179)
j = V2(672, 192)
k = V2(659, 214)
l = V2(615, 214)
m = V2(632, 230)
n = V2(580, 230)
o = V2(597, 215)
p = V2(552, 214)
q = V2(517, 144)
r = V2(466, 180)
s = V2(609, 230)
t = V2(614, 132)

rend.glTriangle(a, r, b,  color(0.13, 0.30, 0.95))
rend.glTriangle(q, r, b,  color(0.13, 0.30, 0.95))
rend.glTriangle(q, c, b,  color(0.13, 0.30, 0.95))
rend.glTriangle(q, c, d,  color(0.13, 0.30, 0.95))
rend.glTriangle(d, g, e,  color(0.13, 0.30, 0.95))
rend.glTriangle(e, g, f,  color(0.13, 0.30, 0.95))
rend.glTriangle(q, d, t,  color(0.13, 0.30, 0.95))
rend.glTriangle(q, p, t,  color(0.13, 0.30, 0.95))
rend.glTriangle(p, o, t,  color(0.13, 0.30, 0.95))
rend.glTriangle(o, l, t,  color(0.13, 0.30, 0.95))
rend.glTriangle(o, n, s,  color(0.13, 0.30, 0.95))
rend.glTriangle(o, s, l,  color(0.13, 0.30, 0.95))
rend.glTriangle(s, l, m,  color(0.13, 0.30, 0.95))
rend.glTriangle(l, k, t,  color(0.13, 0.30, 0.95))
rend.glTriangle(k, j, t,  color(0.13, 0.30, 0.95))
rend.glTriangle(j, i, h,  color(0.13, 0.30, 0.95))
rend.glTriangle(j, h, t,  color(0.13, 0.30, 0.95))
rend.glTriangle(h, t, g,  color(0.13, 0.30, 0.95))
rend.glTriangle(t, d, g,  color(0.13, 0.30, 0.95))

# interior de la taza
u = V2(682, 175)
v = V2(708, 120)
w = V2(735, 148)
z = V2(739, 170)
aa = V2(710, 160)


rend.glTriangle(u, aa, z,  color(0, 0, 0))
rend.glTriangle(z, aa, w,  color(0, 0, 0))
rend.glTriangle(v, aa, w,  color(0, 0, 0))
rend.glTriangle(u, aa, v,  color(0, 0, 0))


rend.glFinish("lab01.bmp")
