class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # first: sanitize array
            # while marking 1s
        
        con1 = False
        n = len(nums)

        # sanitization step
        for i in range(n):
            
            if nums[i] == 1:
                con1 = True
            
            if nums[i] <= 0:
                nums[i] = 1
            elif nums[i] > n:
                nums[i] = 1 

        if not con1:
            return 1
        
        # set kv pairs
            #note we're preserving 0 for values equal to n (which will prompt us to return n+1 later)
        for i in range(n):
            val = abs(nums[i])

            if val == n:
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])
        

        for i in range(1, n):
            if nums[i] > 0:
                return i

        
        if nums[0] > 0:
            return n

        return n+1

        
