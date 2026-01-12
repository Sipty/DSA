class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        ans = []
        n = len(nums)//2

        j = n

        for i in range(0, n, 1):
            ans.append(nums[i])
            ans.append(nums[j])

            j += 1
            
        return ans