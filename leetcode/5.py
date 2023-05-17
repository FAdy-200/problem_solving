# https://leetcode.com/problems/longest-palindromic-substring/description/
from typing import *
from functools import cache
from sys import setrecursionlimit

setrecursionlimit(100000)

# TODO: finish this
class Solution:
    def longestPalindrome1(self, s):
        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        max_len = 0
        ans = [0, 0]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if check(i, j):
                    if j - i > max_len:
                        max_len = j - i
                        ans = [i, j]
        return s[ans[0]:ans[1]]

    def longestPalindrome(self, s):
        dp = [[False] * len(s)] * len(s)
        for i in range(len(s)):
            dp[i][i] = True
        max_len = 1
        ans = s[0]
        for m in range(2, len(s) + 1):

            for i in range(len(s) - m + 1):
                j = i + m - 1
                if s[i] == s[j]:
                    if m == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if m > max_len:
                            ans = s[i:i + m]
                            max_len = m

        return ans
S = Solution()
X = S.longestPalindrome(
    "gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv")
print(X)
