class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        dic = {}

        for i in range(len(nums)):
            leftover = target - nums[i]
            
            if leftover in dic:
                return [i, dic[leftover]]
            else:
                dic[nums[i]] = i