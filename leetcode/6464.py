from typing import *
from collections import defaultdict
from math import gcd
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        graph = defaultdict(set)
        for i,val1 in enumerate(nums):
            for j,val2 in enumerate(nums[i+1:]):
                if gcd(val1,val2) > 1:
                    graph[val1].add(val2)
                    graph[val2].add(val1)
        d = {}
        def traverse(os,s,dist,seen):
            if (s,dist) in d:
                return d[(s,dist)]
            if dist in graph[s]:
                d[(s,dist)] = True
                return True
            seen.add(s)
            blocked = False
            for i in graph[s]:
                if i not in seen:
                    if traverse(os,i,dist,seen.copy()):
                        d[(s,dist)] = True
                        return True
                elif i != os:
                    blocked = True
            if blocked:
                d[(s,dist)] = False
            return False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if not traverse(nums[i],nums[i],nums[j],set()):
                    return False
        return True


S = Solution()
X = S.canTraverseAllPairs([42,98,75,55])
print(X)