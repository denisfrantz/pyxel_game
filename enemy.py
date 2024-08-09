import pyxel
from ship import Ship

class Enemy(Ship):
    def __init__(self, x, y, u, v, w, h):
        super().__init__(x, y, u, v, w, h)
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w

    def moveEnemyShip(self, speed):
        try:
            if speed > 3.2:
                raise Exception("Velocidade ultrapassou o limite!")
        finally:
            self.y += speed