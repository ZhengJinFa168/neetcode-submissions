class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        countT = [0] * 58
        for i in t:
            countT[ord(i)-ord("A")] += 1
        
        have, need = 0,len(t)
        l = r = 0
        window = [0] * 58
        res, lenRes = "",float("infinity")
        while r < len(s):
            pos = ord(s[r])-ord("A")
            if countT[pos] > window[pos]:
                have += 1
            window[pos] += 1
            while have == need:
                if (r - l + 1) < lenRes:
                    lenRes = r - l + 1
                    res = s[l:r+1]
                pos_l = ord(s[l]) - ord("A")
                if countT[pos_l] > 0 and countT[pos_l] == window[pos_l]:
                    have -= 1
                window[pos_l] -= 1
                l += 1
            
            r += 1
        return res

            

    


        