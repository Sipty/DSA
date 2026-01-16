class Solution:
    # def logicCheck(self, left, right):
    #     return (left[0] <= right[0] and right[0] <= left[1]) or (left[0] <= right[1] and right[1] <= left[1])

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # ans = []
        # intervals.sort()

        # for i in range(len(intervals)-1):
        #     left, right = intervals[i], intervals[i+1]
        #     # check if right interval's left boundry belongs to the current interval
        #     if left[0] <= right[0] and right[0] <= left[1]:
        #         tmp = [left[0], left[1], right[0], right[1]]
        #         intervals[i+1] = [min(tmp), max(tmp)]
        #         intervals[i] = [-1, -1]
        
        # for i in range(len(intervals)):
        #     if intervals[i] != [-1, -1]:
        #         ans.append(intervals[i])

        # return ans

        intervals.sort()
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            
            # if we find overelap:
            if ans[-1][1] >= intervals[i][0]:
                ans[-1] = [min(ans[-1][0], intervals[i][0]), max(ans[-1][1], intervals[i][1])]
            else:
                ans.append(intervals[i])
        
        return ans



