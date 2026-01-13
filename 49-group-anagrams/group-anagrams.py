class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # ans = []
        # d_ans = [] # list of dict reprentations for each entry in ans


        # for s in strs:
            
        #     # convert string to dict
        #     d = defaultdict(int)
        #     for char in s:
        #         d[char] += 1

            
        #     exists_in_d_ans = False
        #     # check if exists in d_ans
        #     for i in range(len(d_ans)):
        #         if d == d_ans[i]:
        #             exists_in_d_ans = True
        #             ans[i].append(s)
        #             break

            
        #     # if not in d ans, add it, then separately to ans
        #     if exists_in_d_ans is False:
        #         d_ans.append(d)
        #         ans.append([s])

        # return ans

        d_ans = defaultdict(list)

        for s in strs:

            # check if s is in d_ans, else add it
            st = tuple(sorted(s))

            d_ans[st].append(s)
            
        ans = []
        for d in d_ans:
            ans.append(d_ans[d])
        
        return ans














