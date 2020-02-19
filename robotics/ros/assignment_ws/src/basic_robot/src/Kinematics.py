import math


class Kinematics:

    def __init__(self):
        self.link1 = 1.0
        self.robotHeight = 0.6

    def getInverseKinematics(self, x, y, z):
        t1 = 0.0
        if x != 0.0 or y != 0.0:
            t1 = math.atan2(x, y)
        t2 = 0.0
        height = z - self.robotHeight
        if self.isValidHeight(height):
            t2 = math.asin(height / self.link1)
        return t1, t2

    def getForwardKinematics(self, t1, t2):
        z = self.link1 * math.sin(t2) + self.robotHeight
        x = 0.0
        y = 0.0
        if not z == self.link1 + self.robotHeight:
            x = self.link1 * math.sin(t1)
            y = self.link1 * math.cos(t1)
        return x, y, z

    @staticmethod
    def isValidHeight(height):
        return height <= 1 and height >= -0.4 and height != 0.0
