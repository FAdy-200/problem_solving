# https://leetcode.com/problems/substring-with-largest-variance/
from USEFUL_CODES.LC import *


class Solution:
    def largestVarianceDP(self, s: str) -> int:
        trans = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                 'x': 23, 'y': 24, 'z': 25}
        dp = {}

        def DP(i: int, j: int, arr: List[int]):
            if (x := (i, j)) in dp:
                return dp[x]
            if i >= j or sum(arr) <= 0:
                return 0
            ma = -inf
            mi = inf
            for l_i in arr:
                if l_i and l_i > ma:
                    ma = l_i
                if l_i and l_i < mi:
                    mi = l_i
            l_ans = ma - mi
            arr[trans[s[i]]] -= 1
            if l_ans < (t1 := DP(i + 1, j, arr[:])):
                l_ans = t1

            arr[trans[s[j]]] -= 1
            if l_ans < (t2 := DP(i + 1, j - 1, arr[:])):
                l_ans = t2
            arr[trans[s[i]]] += 1
            if l_ans < (t3 := DP(i, j - 1, arr[:])):
                l_ans = t3
            dp[x] = l_ans
            return dp[x]

        temp = [0] * 26
        for item in s:
            temp[trans[item]] += 1
        return DP(0, len(s) - 1, temp)

    def largestVariance(self, s: str) -> int:
        dp = Counter(s)

        def calc(c1: str, c2: str) -> int:
            ma = 0
            mi = 0
            remain = dp[c2]
            b_ma = -inf

            for ch in s:
                if ch == c1:
                    ma += 1

                if ch == c2:
                    mi += 1
                    remain -= 1

                if mi > 0:
                    if ma - mi > b_ma:

                        b_ma = ma - mi

                if ma < mi and remain > 0:
                    ma = 0
                    mi = 0
            return b_ma

        alpha = "abcdefghijklmnopqrstuvwxyz"
        ans = 0
        for val_1 in alpha:
            for val_2 in alpha:
                if val_1 in s and val_2 in s and val_1 != val_2:
                    if (x := calc(val_1, val_2)) > ans:
                        ans = x
        return ans


S = Solution()
X = S.largestVariance(
    "lucmdweawziyvixyfesksmkxkbzzzqdmrmvdxeghlrlyteuhvumwppwltssrlboozoiudqegobjvnuinwoaaxbiqivtwabunqkzvjnczasvghsvrc"
    "kpzelcqeloppxwmnbeocoiximllpvhahesjxznfphohoycaqsaghpoligtghoejodmhwuzjmpwkrpehheuubiespninbzfbqtiimtzbymdrxxbjzh"
    "qanmoocicqfhdrtfwjbxkgehjdqhmmjnrrgilsvyhonfmvywaejhxxgabogdqgttfiufrgpgpduwhzgmgoecwagwdvmnobiukuigphrkupqkeaphj"
    "sqhmetkgmcramydkosqqmayrdgfiokpanxznuknqpcqsbumyrxfsmmcxvherbjykpbwdzeqjgdhysauxflcdhkmlflmygylnxubaimtmsbbapfsrq"
    "dwwihubmemmhumzhmvalwkneehsxjofrcubyscgmlwfuzepmlyvpthqlvxrzcekmbemneozbtfajwkaizheoexbtdicgzmgnbytwyruexhigheujn"
    "olqafjmvtfgeduwtkisjovklsazfoslylmqjkgafbcfsawdjlyyobskeywidozxbmmapjrhqjjtoknpujwibccdotmnfxqcmhbelrireqfxmqoitc"
    "iszlhecacxrpdbxeqravhrgwylhzpamvjjmghrzywpfpxjogidkkuolqscxuqgxzfmkuiagndjfhcmuwysojjmwtdrmicpnjpxonymsuwvrodwmfb"
    "tpwyxmesmkpuctrlabbknyoyueumfitkpdzsnkurzzyexeutmbqcdbmirqndghaksbpukszbkgvgswjrixuwvzsoymjuiungsnpytstwjbekzudtj"
    "xqkwkhgyophfllqvmdwvdlywtnsvlfwkesxdhdfwytgtwkgprlocjlcjqezcwpiwldnrqwyqxrgyyrkdotjhtsppwjkpecnpyarjftdbvzhdnqkqp"
    "bkwtkcfsomzwgxnwtsoslvxbwdkfvaeyxzkadctnngewqbwftphtfcdhjbwzytmrlolbgouoluyfyngtkijgwvxmjzqcapymvdssiirusnrnmuext"
    "feosrdsudwixozufmwatfmjjumqmnprsqdrrerjkivjlnohkgckhuzbajvfjezbsivnhnexfryxghcxvetlwnjlutskdguwlsqhcuravxvfmzeycx"
    "ifyjjqvbdmlmzfsuekrszqvdtmlfcytznjkplqpveqybkdmggrnyuoabxkepgbenzaufxwrmqufmnlgndjakvhbkkkzhgdoutdphnrqhtogbrpgdi"
    "fgcqzheognwlgoqszqjsshaiciiwjqoxlznfgjtytrmkmypspmmsyencfxdjtzzlzgjzzoqwkzriqhvfqigezstcwcflbhyalipesdxddoyzcdskt"
    "hyiasfdkgxgigirbixeaneynxedrbvfybpxxonssjylrahpkklrjgvbzllsfinxtcdkejynhxekkehqlizormtlmglsakfrketakpgsziogdgtfpw"
    "zeufejryluxjjuwfcgvbipmkrgtnfupqshysughfgnxtfgazdybvdtiqiimxibxlxhzsorqgshaauhgjszlfhaoxzfhnnfsdnsxqjmhaliuhavzqi"
    "elpcqjzbzelrnruhqzxrynexubqpkhsoqrearfdxmliaiamfaorysjpuldzvuqnddmskegfmrxdgeonfhyuzhpgmghsvkvolhvrdyqvgqxshjjzro"
    "zkhkrsoktmvpkllizosqdsmybnwmybkyfqxyaeumgcubtdwtlbxuhcowgqvvrraazmeoamazjbljfzfvjmjhiifpskinydncsbcoefknvjzqinbfv"
    "gyyfjzqewxwdzivzeemqvxmjrsuxavjeqtbklezsqeas"
)
print(X)
