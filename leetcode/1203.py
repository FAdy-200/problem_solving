# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
from typing import List, DefaultDict, Set, Dict
from collections import defaultdict
from USEFUL_CODES.GraphFunctions import topological_sort


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """
        We start by creating a new representation for the groups using dictionaries where each `groups[groupId]` is a set of all nodes with `id == groupId`, and we create a new group for each node that is not in any group.
        Then we find the dependencies within each group and between groups.
        lastly we sort each group by itself using the dependencies between the nodes inside said group, and the groups by their id using the between groups dependency topologically and merge the results.
        Time: O(n)
        Space: O(n)
        """
        groups: DefaultDict[int, Set[int] | List[int]] = defaultdict(set)
        groups_out_dep: DefaultDict[int, Set] = defaultdict(set)
        groups_in_dep: DefaultDict[int, DefaultDict[int, Set[int]]] = defaultdict(lambda: defaultdict(set))
        # Creating the new representation
        for i in range(n):
            groups[group[i]].add(i)
        # adding a new group for each of the -1 nodes
        ma = max(groups)
        for i, j in enumerate(groups[-1]):
            groups[ma + i + 1] = [j]
            group[j] = ma + i + 1
        groups.pop(-1)

        # Creating the dependency Hash maps
        for i in range(n):
            for j in beforeItems[i]:
                if j not in groups[group[i]]:
                    groups_out_dep[group[j]].add(group[i])
                else:
                    groups_in_dep[group[i]][j].add(i)

        # Sorting each group
        sorted_groups: Dict[int, List[int]] = {}
        for i, j in groups.items():
            if len(temp := topological_sort(j, groups_in_dep[i])) == len(j):
                sorted_groups[i] = temp
            else:
                return []

        # Sorting the groups by their id
        if len((sorted_all := topological_sort(set(groups.keys()), groups_out_dep))) != len(sorted_groups):
            return []

        # creating the final answer array
        ans = []
        for i in sorted_all:
            ans += [*sorted_groups[i]]
        return ans


S = Solution()
X = S.sortItems(5
                , 5
                , [2, 0, -1, 3, 0]
                , [[2, 1, 3], [2, 4], [], [], []])
print(X)
