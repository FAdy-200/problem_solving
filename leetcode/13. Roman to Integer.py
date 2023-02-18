class Solution:
    def romanToInt(self, s: str) -> int:
        dict_map = {
        "":0,
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
        ans = 0
        
        i = 0
        while i<len(s):
            pair = s[i:i+2]
            if len(pair)==2:
                if dict_map[pair[1]]>dict_map[pair[0]]:
                    
                    ans+=dict_map[pair[1]] - dict_map[pair[0]]
                    i+=2
                else:
                    ans+=dict_map[pair[0]]
                    i+=1
            else:
                ans+=dict_map[pair[0]]
                i+=1

        
        return ans

        



s = Solution()
x = s.romanToInt("VIV")
print(x)