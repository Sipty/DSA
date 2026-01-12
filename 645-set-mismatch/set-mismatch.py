class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        # return vals are: [duplicate_number, missing_number]
        map = defaultdict(int)
        missing_number = 0
        duplicate_number = 0
        
        # build hashi map
        for n in nums:
            map[n] += 1  

        for i in range(len(nums)):
            # find missing number via hash map
            if map[i+1] == 0:
                missing_number = i+1
            
            # find dup number via hash map
            if map[i+1] > 1:
                duplicate_number = i+1 

        return [duplicate_number, missing_number]

