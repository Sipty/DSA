class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        d = int(len(logs)//2)
        result = [0] * n
        stack = deque()
        prev = 0

        for log in logs:
            tmp = log.split(":")
            id, timestamp = int(tmp[0]), int(tmp[2])

            if tmp[1] == "start":

                if stack:
                    # add the block time
                    result[stack[-1]] += timestamp - prev
                
                stack.append(id)
                prev = timestamp
            else:
                stack.pop()
                result[id] += timestamp - prev + 1
                prev = timestamp +1
            
            



        
        return result