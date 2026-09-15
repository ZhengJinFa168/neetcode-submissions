class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            base = r - l
            area = base * min(heights[l],heights[r])
            if area > max_area:
                max_area = area
            if heights[l]>heights[r]:
                r -= 1
            else:
                l += 1
        return max_area