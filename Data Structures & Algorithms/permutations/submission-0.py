class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, seen):
            if len(path) == len(nums):
                res.append(path[:])  
                return
            for i in range(len(nums)):
                if seen[i]:
                    continue
                path.append(nums[i])
                seen[i] = True

                backtrack(path,seen)

                path.pop()
                seen[i] = False
            
        backtrack([],[False]*len(nums))
        return res

                
            