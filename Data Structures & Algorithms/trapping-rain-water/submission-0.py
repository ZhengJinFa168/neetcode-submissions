class Solution:
    def trap(self, height: List[int]) -> int:
        max_prefix = []
        max_l = 0
        max_suffix = []
        max_r = 0
        res = 0
        for i in height:
            max_prefix.append(max_l)
            if i > max_l:
                max_l = i
        for i in range(len(height)-1,-1,-1):
            max_suffix.append(max_r)
            if height[i] > max_r:
                max_r = height[i]
        for i in range(len(height)):
            water_at_i = min(max_suffix[len(height)- 1 - i],max_prefix[i]) - height[i]
            if water_at_i < 0:
                water_at_i = 0
            res += water_at_i

        return res
            
