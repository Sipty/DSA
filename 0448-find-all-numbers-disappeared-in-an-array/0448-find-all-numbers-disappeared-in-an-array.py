class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # ans = []
        # # find len of nums
        # n = len(nums)
        # # create set of nums
        # snums = set(nums)
        # # itter over nums and return vals not in snums
        # for i in range(1, n+1):
        #     if i not in snums:
        #         ans.append(i)
        
        # return ans

        for i in range(len(nums)):
            cur_num = abs(nums[i])
            
            nums[cur_num-1] = -abs(nums[cur_num-1])

        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        
        return ans