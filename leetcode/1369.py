# https://leetcode.com/problems/design-underground-system/
from collections import defaultdict
from typing import Dict, DefaultDict, Tuple, List


class UndergroundSystem:

    def __init__(self):
        self.old: DefaultDict[str, List[int, int]] = defaultdict(lambda: [0, 0])
        self.ongoing: Dict[int, Tuple[str, int]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ongoing[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        oldStation, oldTime = self.ongoing[id]
        self.old[oldStation + " -> " + stationName][0] += t - oldTime
        self.old[oldStation + " -> " + stationName][1] += 1
        self.ongoing.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        su, nu = self.old[startStation + " -> " + endStation]
        return su / nu

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
