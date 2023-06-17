import configparser

from config.config import *


class Config:
    def __init__(self, custom=CUSTOM_CONFIG):
        self.startcolor = STARTCOLOR
        self.visitedcolor = VISITEDCOLOR
        self.bordercolor = BORDERCOLOR
        self.maincolor = MAINCOLOR
        self.width, self.heigh = INIT_WIDTH, INIT_HEIGHT
        self.fps = FPS
        self.level = 1
        self.config = custom

    def cellsize_level(self):
        cellsize = CELLSIZE
        if self.level != 1:
            cell = self.heigh // CELLSIZE + 5 * self.level
            cellsize = self.heigh // cell
        return cellsize

    def config_load(self):
        config = configparser.ConfigParser()
        config.read('config/config.ini')

    def config_save(self):
        config = configparser.ConfigParser()
        config.read('config/config.ini')

        with open('config.ini', 'w') as configfile:
            config.write(configfile)
