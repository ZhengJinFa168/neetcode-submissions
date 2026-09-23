class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        max_l = height[l]
        r = len(height) - 1
        max_r = height[r]
        res = 0
        while l < r:
            if max_l <= max_r:
                l += 1
                water_at_i = min(max_l,max_r) - height[l]
                if water_at_i < 0:
                    water_at_i = 0
                res += water_at_i
                if height[l]>max_l:
                    max_l = height[l]
            else:
                r -= 1
                water_at_i = min(max_l,max_r) - height[r]
                if water_at_i < 0:
                    water_at_i = 0
                res += water_at_i
                if height[r]>max_r:
                    max_r = height[r]

        return res
                
            