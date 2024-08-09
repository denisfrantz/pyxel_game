import pyxel

def centerText(text, page_w, char_w = pyxel.FONT_WIDTH):
    text_w = len(text) * char_w
    return (page_w - text_w) / 2

class Hud:
    def __init__(self):
        self.title = "SPACESHIP WARS"
        self.youWon = "VICTORY"
        self.youLost = "GAME OVER"
        self.quit = "QUIT"
        self.pressQ = "-> PRESS Q"
        self.title_x = centerText(self.title, pyxel.width)
        self.youWon_x = centerText(self.youWon, pyxel.width)
        self.youLost_x = centerText(self.youLost, pyxel.width)
        self.quit_x = centerText(self.quit, pyxel.width)
        self.pressQ_x = centerText(self.pressQ, pyxel.width)
    
    def drawTitle(self):
        pyxel.rect(0, 0, pyxel.width, 30, pyxel.COLOR_BLACK)
        pyxel.text(self.title_x, 1, self.title, pyxel.COLOR_GREEN)

    def drawLives(self, u, v, w, h):
        pyxel.text(14, 10, "LIVES", pyxel.COLOR_GREEN)
        pyxel.blt(4, 16, 0, u, v, w, h)

    def drawLevel(self, level):
        pyxel.text(100, 10, "LEVEL", pyxel.COLOR_GREEN)
        pyxel.text(108, 16, level, pyxel.COLOR_GREEN)

    def drawYouWon(self):
        pyxel.text(self.youWon_x, pyxel.height/3, self.youWon, pyxel.COLOR_YELLOW)
        pyxel.text(self.quit_x, pyxel.height-20, self.quit, pyxel.COLOR_LIME)
        pyxel.text(self.pressQ_x, pyxel.height-10, self.pressQ, pyxel.COLOR_LIME)

    def drawYouLost(self):
        pyxel.text(self.youLost_x, pyxel.height/3, self.youLost, pyxel.COLOR_RED)
        pyxel.text(self.quit_x, pyxel.height-20, self.quit, pyxel.COLOR_LIME)
        pyxel.text(self.pressQ_x, pyxel.height-10, self.pressQ, pyxel.COLOR_LIME)