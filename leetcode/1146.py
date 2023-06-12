# https://leetcode.com/problems/snapshot-array/
from USEFUL_CODES.LC import *


class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = {i:[[-1,0]] for i in range(length)}
        self.n = 0
    def set(self, index: int, val: int) -> None:

        if self.snaps[index][0] == self.n:
            self.snaps[index][1] = val
        else:
            self.snaps[index].append([self.n,val])

    def snap(self) -> int:
        self.n += 1
        return self.n - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[index][bisect.bisect_left(self.snaps[index],[snap_id + 1,0])-1][1]


snapshotArr = SnapshotArray(2)
snapshotArr.set(0,12)
snapshotArr.snap()
snapshotArr.snap()
snapshotArr.set(1,16)
snapshotArr.snap()
snapshotArr.snap()
snapshotArr.get(1,4)
snapshotArr.get(1,0)
snapshotArr.snap()
snapshotArr.snap()
# print(x, y, z, m)
