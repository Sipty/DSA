class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        numsort = sorted(nums)
        map = {}

        ans = []

        for i in range(len(numsort)):
            if numsort[i] not in map:
                map[numsort[i]] = i

        for i in range(len(nums)):
            ans.append(map[nums[i]])
        
        return ans