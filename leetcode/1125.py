# https://leetcode.com/problems/smallest-sufficient-team/
from USEFUL_CODES.LC import *


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        n_p = len(people)
        mask_people = []
        for p in people:
            mask_people.append(0)
            for skill in p:
                if skill in req_skills:
                    mask_people[-1] |= 1 << req_skills.index(skill)

        @cache
        def DP(i: int, mask: int) -> List[int]:
            if mask == (2 ** n) - 1:
                return [-1]
            if i >= n_p:
                return []
            ans = []
            if (t:=mask | mask_people[i]) != mask:
                if z := DP(i + 1, t):
                    if z != [-1]:
                        if not ans or len(z) < len(ans):
                            ans = z + [i]
                    else:
                        ans = [i]
            if x := DP(i + 1, mask):
                if x != [-1]:
                    if not ans or len(x) < len(ans):
                        ans = x

            return ans

        return DP(0, 0)


S = Solution()
X = S.smallestSufficientTeam(
    ["zp", "jpphhnhwpw", "pscleb", "arn", "acrsxqvus", "fseqih", "fpqbjbbxglivyonn", "cjozlkyodt", "mvtwffgkhjrtibto",
     "kumdvfwsvrht", "i", "s", "ucr", "oo", "yqkqkhhhwngyjrg", "odiwidzqw"],
    [["acrsxqvus"], ["zp"], [], ["fpqbjbbxglivyonn"], [], [], ["kumdvfwsvrht"], [], ["oo"], [], ["fseqih"], [], [
        "arn"], [], [], ["yqkqkhhhwngyjrg"], [], [], [], ["kumdvfwsvrht"], ["s"], [], [], ["zp", "ucr"], [], [
         "pscleb"], [], [], [], [], [], [], [], ["jpphhnhwpw"], [], [], [], ["oo"], [], ["i"], [
         "pscleb"], [], [], [], [], [], [], ["i"], [], ["mvtwffgkhjrtibto", "odiwidzqw"], [], ["cjozlkyodt",
                                                                                               "odiwidzqw"], [
         "arn"], [], [], ["acrsxqvus"], [], [], [], ["ucr"]])
print(X)
