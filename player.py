import pyxel
from ship import Ship

class Player(Ship):
    def __init__(self, x, y, u, v, w, h):
        super().__init__(x, y, u, v, w, h)
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
    
    def movePlayerShip(self, player_speed=1):
        try:
            if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_D):
                raise Exception("Use as setinhas para movimentar a nave!")
        finally:
            if pyxel.btn(pyxel.KEY_UP) and self.y - player_speed - 8 > 0:
                self.y -= player_speed
            if pyxel.btn(pyxel.KEY_DOWN) and self.y + player_speed + 8 < pyxel.height:
                self.y += player_speed
            if pyxel.btn(pyxel.KEY_RIGHT) and self.x + player_speed + 8 < pyxel.width:
                self.x += player_speed
            if pyxel.btn(pyxel.KEY_LEFT) and self.x - player_speed > 0:
                self.x -= player_speed