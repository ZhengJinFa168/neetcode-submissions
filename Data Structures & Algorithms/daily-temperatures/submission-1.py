class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack or temperatures[i]<=stack[-1][0]:
                stack.append([temperatures[i],i])
            else:
                while len(stack)>0 and stack[-1][0]<temperatures[i]:
                    temp = stack.pop()
                    res[temp[1]] = i - temp[1]
                    
                stack.append([temperatures[i],i])
        return res