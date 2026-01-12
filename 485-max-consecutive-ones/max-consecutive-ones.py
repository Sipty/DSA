class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        streak, max_streak = 0, 0

        for n in nums:
            if n == 1:
                streak += 1
                if max_streak < streak:
                    max_streak = streak
            else:
                streak = 0
        
        return max_streak