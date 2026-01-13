class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) < 2:
            return s

        longest, wl, wr = 0, 0, 0

        for i in range(len(s)):
            
            # handle uneven length palindromes
            left, right = i-1, i+1
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left > longest:
                    wl, wr = left, right
                    longest += 1

                left -= 1
                right += 1
            
            # handle even length palindromes
            left, right = i, i+1
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left > longest:
                    wl, wr = left, right
                    longest += 1

                left -= 1
                right += 1
        
        return s[wl:wr+1]