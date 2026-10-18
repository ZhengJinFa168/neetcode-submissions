class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed)==0:
            return True
        
        j = i = 0
        visited = [0]*len(pushed)
        stack = []
        while j < len(popped) and i < len(pushed):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            i += 1
        
        return True if j==len(popped) else False
