class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r = 0, len(people)-1
        res = 0
        while l<=r:
            if l == r:
                res += 1
                break
            diff = limit - people[r]
            if people[l]<=diff:
                l +=1
            res += 1
            r -= 1
        
        return res
