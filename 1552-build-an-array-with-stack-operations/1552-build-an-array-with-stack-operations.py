class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        ans = []
        tarL = len(target)

        for i in range(1, n+1):
            if i in target:
                ans.append("Push")
                tarL -= 1
            else:
                ans.append("Push")
                ans.append("Pop")
            
            if tarL == 0:
                return ans