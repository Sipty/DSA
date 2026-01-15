class Solution:
    # def merge(self, left, right):
    #     tmp = [left[0], left[1], right[0], right[1]]
    #     return [min(tmp), max(tmp)]

    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
    #     ans = []

    #     for interval in intervals:

    #         if newInterval[1] < interval[0]:
    #             # self.merge newInterval against ans 
    #             if newInterval != [-1,-1]:
    #                 if ans == []:
    #                     ans.append(newInterval)
    #                 elif ans[-1][1] >= newInterval[0]:
    #                     ans[-1] = self.merge(ans[-1], newInterval)
    #                 else:
    #                     ans.append(newInterval)
                    
    #                 newInterval = [-1,-1]
                
    #             # self.merge interval into ans
    #             if ans[-1][1] >= interval[0]:
    #                 ans[-1] = self.merge(ans[-1], interval)
    #             else:
    #                 ans.append(interval)


    #         elif interval[1] < newInterval[0]:
    #             # self.merge interval into ans
    #             if ans == []:
    #                 ans.append(interval)
    #             elif ans[-1][1] >= interval[0]:
    #                 ans[-1] = self.merge(ans[-1]), interval
    #             else:
    #                 ans.append(interval)

    #         else:
    #             # self.merge interval and newInterval, before merging into ans
    #             interval = self.merge(newInterval, interval)
                
    #             if ans == []:
    #                 ans.append(interval)
    #             elif ans[-1][1] >= interval[0]:
    #                 ans[-1] = self.merge(ans[-1]), interval
    #             else:
    #                 ans.append(interval)
                
    #             newInterval = [-1,-1]

    #     if newInterval != [-1,-1]:
    #         if ans == []:
    #             ans.append(newInterval)
    #         elif ans[-1][1] >= newInterval[0]:
    #             ans[-1] = self.merge(ans[-1]), interval
    #         else:
    #             ans.append(newInterval)


    #     return ans

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)

        return res






