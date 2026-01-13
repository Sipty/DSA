class Solution:
    def isPalindrome(self, s: str) -> str:

        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        
        return True


    def longestPalindrome(self, s: str) -> str:
        l = len(s)

        if l <= 1:
            return s

        while l > 0:
            
            left, right = 0, l-1

            while right < len(s):

                if self.isPalindrome(s[left:right+1]):
                    return s[left:right+1]
                else:
                    left += 1
                    right += 1


            l -= 1



        
        return s

















