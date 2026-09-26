class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = [0] * 26
        for i in s1:
            counter[ord(i) - ord("a")] += 1
        l = 0
        r = len(s1)
        while l < len(s2) - len(s1) + 1:
            temp = [0] * 26
            for i in range(l,r):
                temp[ord(s2[i])-ord("a")] += 1
            if temp == counter:
                return True
            l += 1
            r += 1

        return False

            


