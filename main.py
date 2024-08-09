import pyxel
import random
from hud import Hud
from ship import Ship
from player import Player
from enemy import Enemy
from soundtrack import Soundtrack

class Game:
    def __init__(self):
        pyxel.init(128, 160, title = "SPACESHIP WARS", fps = 60)
        pyxel.load("my_resource.pyxres")
        self.hud = Hud()
        self.soundtrack = Soundtrack()
        self.enemies = []
        self.wave_len = 0
        self.level = 0
        self.lives = 5
        self.enemy_speed = 0.8
        self.player = Player((128/2)-8, pyxel.height-16, 0, 32, 8, 8)
        self.enemy = Enemy(0, 0, 0, 0, 0, 0)
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.level == 11 or self.lives == 0:
            return
        else:
            self.spawnEnemies()
            self.moveEnemies()
            self.player.movePlayerShip()

    def draw(self):
        pyxel.bltm(0, 30, 0, 0, 0, pyxel.width, pyxel.height)
        self.drawEnemies()
        self.player.drawShip()
        self.hud.drawTitle()
        self.checkLives()
        self.checkLevel()

    def drawEnemies(self):
        for enemy in self.enemies:
            enemy.drawShip()

    def spawnEnemies(self):
        if len(self.enemies) == 0:
            self.level += 1
            self.wave_len += 1
            self.enemy_speed += 0.2
            for i in range(self.wave_len):
                cd_v = random.randint(0, 3)
                enemy = Enemy(random.randint(0, 120), random.randint(-100, 0), 0, 8*cd_v, 8, 6)
                self.enemies.append(enemy)
        
    def moveEnemies(self):
        for enemy in self.enemies[:]:
            enemy.moveEnemyShip(self.enemy_speed)
            if enemy.y + 6 > pyxel.height:
                self.enemies.remove(enemy)
        for enemy in self.enemies[:]:
            for y1 in range(int(enemy.y), int(enemy.y+6)):
                for y2 in range(int(self.player.y), int(self.player.y+8)):
                    if (y1 == y2) or (y1+6 == y2) or (y1 == y2+8):
                        for x1 in range(int(enemy.x), int(enemy.x+8)):
                            for x2 in range(int(self.player.x), int(self.player.x+8)):
                                if x1 == x2:
                                    if enemy in self.enemies:
                                        self.enemies.remove(enemy)
                                        self.lives -= 1
                                        self.soundtrack.playDeathSound()

    def checkLives(self):
        if self.lives == 5:
            self.hud.drawLives(0, 48, 40, 7)
        elif self.lives == 4:
            self.hud.drawLives(0, 56, 32, 7)
        elif self.lives == 3:
            self.hud.drawLives(0, 64, 24, 7)
        elif self.lives == 2:
            self.hud.drawLives(0, 72, 16, 7)
        elif self.lives == 1:
            self.hud.drawLives(0, 80, 8, 7)
        elif self.lives == 0:
            pyxel.cls(pyxel.COLOR_BLACK)
            self.hud.drawTitle()
            self.hud.drawYouLost()
            if pyxel.btn(pyxel.KEY_Q):
                pyxel.quit()

    def checkLevel(self):
        if self.level == 1 and self.lives > 0:
            self.hud.drawLevel("1")
        elif self.level == 2 and self.lives > 0:
            self.hud.drawLevel("2")
        elif self.level == 3 and self.lives > 0:
            self.hud.drawLevel("3")
        elif self.level == 4 and self.lives > 0:
            self.hud.drawLevel("4")
        elif self.level == 5 and self.lives > 0:
            self.hud.drawLevel("5")
        elif self.level == 6 and self.lives > 0:
            self.hud.drawLevel("6")
        elif self.level == 7 and self.lives > 0:
            self.hud.drawLevel("7")
        elif self.level == 8 and self.lives > 0:
            self.hud.drawLevel("8")
        elif self.level == 9 and self.lives > 0:
            self.hud.drawLevel("9")
        elif self.level == 10 and self.lives > 0:
            self.hud.drawLevel("10")
        elif self.level == 11:
            pyxel.cls(pyxel.COLOR_BLACK)
            self.hud.drawTitle()
            self.hud.drawYouWon()
            if pyxel.btn(pyxel.KEY_Q):
                pyxel.quit()

if __name__ == "__main__":
    Game()