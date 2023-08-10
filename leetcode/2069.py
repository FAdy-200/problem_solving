# https://leetcode.com/problems/walking-robot-simulation-ii/
from USEFUL_CODES.LC import *
class Robot:

    def __init__(self, width: int, height: int):
        self.pos = 0
        self.dir = 0
        self.dirs = {0: "East", 1: "North", 2: "West", 3: "South"}
        self.width = width - 1
        self.height = height - 1
        self.mid = height + width - 2

    def step(self, num: int) -> None:
        self.pos += num
        self.pos %= (self.mid * 2)
        if self.pos > self.mid + self.width:
            self.dir = 3
        elif self.pos > self.mid:
            self.dir = 2
        elif self.pos > self.width:
            self.dir = 1
        elif not self.pos:
            self.dir = 3
        else:
            self.dir = 0

    def getPos(self) -> List[int]:
        if self.pos > self.mid + self.width:
            return [0,self.height - (self.pos - self.mid - self.width)]
        elif self.pos > self.mid:
            return [self.width - (self.pos - self.mid) ,self.height]
        elif self.pos > self.width:
            return [self.width, self.pos - self.width ]
        else:
            return [self.pos,0]

    def getDir(self) -> str:
        return self.dirs[self.dir]
# Your Robot object will be instantiated and called as such:
obj = Robot(20, 14)
obj.step(32+18+18+18+45+37+39+8+11+18)
param_2 = obj.getPos()
param_3 = obj.getDir()
