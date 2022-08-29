# Table Class
# -----------
# Author: Pau López Ribas (paulopezribas@gmail.com)
# Date: 2022/08/23
# Description: Defines the area where the robot can move arround.


import numpy as np

class Table:
    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)
        self.faces = np.array(['EAST', 'NORTH', 'WEST', 'SOUTH'])

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getFaces(self):
        return self.faces

    def setX(self, x):
        self.x = int(x)

    def setY(self, y):
        self.y = int(y)

    # The table could be more complex, for instance with blocked areas
    # to drive into