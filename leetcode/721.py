# https://leetcode.com/problems/accounts-merge/
from typing import List, DefaultDict, Set, Dict
from collections import defaultdict

class Solution:
    def accountsMergeHack(self, x: List[List[str]]) -> List[List[str]]:
        def helper(accounts):
            emails: DefaultDict[str, int] = defaultdict(lambda: -1)
            ref: DefaultDict[int, int] = defaultdict(lambda: -1)
            for i, val in enumerate(accounts):
                for j in val[1:]:
                    if emails[j] >= 0:
                        if ref[emails[j]] >= 0:
                            ref[i] = ref[emails[j]]
                        else:
                            ref[i] = emails[j]
                    else:
                        emails[j] = i
            ans_emails: DefaultDict[int, Set] = defaultdict(set)
            names: Dict[int, str] = {}
            for i, val in enumerate(accounts):
                ind = i
                if ref[i] >= 0:
                    ind = ref[i]
                names[ind] = val[0]
                for j in val[1:]:
                    ans_emails[ind].add(j)
            ans = []
            for i, j in names.items():
                ans.append([j, *list(sorted(ans_emails[i]))])
            return ans

        return helper(x)

    def accountsMerge(self, x: List[List[str]]) -> List[List[str]]:
        graph = {i: i for i in range(len(x))}

        def find_root(a: int) -> List[int]:
            lans = [a]
            while graph[lans[-1]] != lans[-1]:
                lans.append(graph[lans[-1]])
            return lans

        def join(a: int, b: int) -> None:
            roots_a = find_root(a)
            roots_b = find_root(b)
            for i in roots_a:
                graph[i] = roots_a[-1]
            for i in roots_b:
                graph[i] = roots_a[-1]

        nacc: DefaultDict[str, Dict[int, Set]] = defaultdict(dict)
        for i, val in enumerate(x):
            nacc[val[0]][i] = set(val[1:])
        for val in nacc.values():
            for i, j in val.items():
                for m, k in val.items():
                    if m <= i:
                        continue
                    if len(j.intersection(k)):
                        join(i, m)

        for i, j in graph.items():
            join(i, j)
        dict_ans: DefaultDict[int, Set] = defaultdict(set)
        for i, j in graph.items():
            for val in x[i][1:]:
                dict_ans[j].add(val)

        ans = []

        for i, j in dict_ans.items():
            ans.append([x[i][0], *list(sorted(j))])
        return ans


S = Solution()
X = S.accountsMerge(
    [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
     ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
     ["David", "David1@m.co", "David2@m.co"]])

print(X)
