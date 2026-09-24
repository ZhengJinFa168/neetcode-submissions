class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        l = len(heights)
        for i in range(l):
            print(heights[i])
            if not stack or heights[i]>=stack[-1][1]:
                stack.append([i,heights[i]])
            else:
                while stack and heights[i] < stack[-1][1]:
                    temp = stack.pop()
                    index, popped_h = temp[0],temp[1]
                    base = i - index
                    area = base * popped_h
                    if area > maxArea:
                        maxArea = area
                stack.append([index,heights[i]])
        
        while stack:
            temp = stack.pop()
            index, popped_h = temp[0],temp[1]
            base = l - index
            area = base * popped_h
            if area > maxArea:
                maxArea = area
        return maxArea