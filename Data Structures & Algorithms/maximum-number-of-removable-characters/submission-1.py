class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        if not removable:
            return 0
        if len(p) == len(s):
            return 0

        def isSubsequence(k:int):

            seen = set(removable[:k])
            j=0
            for i in range(len(s)):
                if i in seen:
                    continue
                if s[i] == p[j]:
                    j+=1
                    if j == len(p):
                        return True
            return False
        l, r = 0, len(removable)
        ans = 0
        while l <= r:
            mid = (l+r) // 2
            if isSubsequence(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans