class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for i in range(len(nums)):
            leftover = target - nums[i]
            
            if leftover in dic:
                return [i, dic[leftover]]
            else:
                dic[nums[i]] = i