from typing import List, DefaultDict, Set, Dict, Deque
from collections import defaultdict, deque


def topological_sort(nodes: Set, dep: Dict[int, Set[int]] | DefaultDict[int, Set[int]]) -> List[int]:
    """
    Topological sort using number of in bound edges order

    :param nodes: Set of the nodes to be sorted
    :param dep: dependency hashmap
    :return: Sorted list of the given nodes
    """
    in_ord: DefaultDict[int, int] = defaultdict(int)
    for li in nodes:
        if li in dep:
            for lj in dep[li]:
                in_ord[lj] += 1
    ans: List[int] = []
    d:Deque = deque()
    for li in nodes:
        if not in_ord[li]:
            d.append(li)
    while d:
        ans.append(d.popleft())
        for li in dep[ans[-1]]:
            in_ord[li] -= 1
            if not in_ord[li]:
                d.append(li)

    return ans
