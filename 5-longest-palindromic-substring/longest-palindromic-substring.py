class Solution:
    def isPalindrome(self, s: str) -> str:

        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        
        return True


    def longestPalindrome(self, s: str) -> str:

        # basic idea:
        # two pointer, check isPalindrome at each step. 
        # first match - return :)  

        if len(s) == 1:
            return s

        longest = ""

        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                j = i + length
                if self.isPalindrome(s[i:j]):
                    if len(longest) < len(s[i:j]):
                        longest = s[i:j]
            
            if longest != "":
                return longest
        
        return longest