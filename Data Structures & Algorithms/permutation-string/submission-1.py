class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        l = 0
        sorted_s = "".join(sorted(s1))
        while l < len(s2) - len(s1) + 1:
            sorted_s2 = "".join(sorted(s2[l:r]))
            if sorted_s2 == sorted_s:
                return True
            l += 1
            r += 1
        
        return False