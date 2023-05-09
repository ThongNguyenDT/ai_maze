from config.config import *


class Config:
    def __init__(self, custom=CUSTOM_CONFIG):
        self.startcolor = STARTCOLOR
        self.visitedcolor = VISITEDCOLOR
        self.bordercolor = BORDERCOLOR
        self.width = INIT_WIDTH
        self.heigh = INIT_HEIGHT
        self.fps = FPS
        self.level = 1
        self.config = custom

    def cellsize(self):
        cellsize = CELLSIZE
        if self.level != 1:
            cell = self.heigh // CELLSIZE + 5 * self.level
            cellsize = self.heigh // cell
        return cellsize
