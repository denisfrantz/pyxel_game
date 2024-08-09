import pyxel

class Ship:
    def __init__(self, x, y, u, v, w, h):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h

    def drawShip(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, pyxel.COLOR_BLACK)