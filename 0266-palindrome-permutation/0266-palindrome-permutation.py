from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        dic = defaultdict(int)

        for char in s:
            dic[char] += 1
        
        unevens = 0
        for key in dic.keys():
            if dic[key] % 2 != 0:
                if unevens > 0:
                    return False
                else:
                    unevens += 1
        
        return True