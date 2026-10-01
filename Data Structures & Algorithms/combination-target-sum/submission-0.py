class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sorted_arr = sorted(nums)
        def dfs(i, path, total):
            if total == target:
                res.append(path[:])
            
            if total >= target or i >= len(nums):
                return

            path.append(sorted_arr[i])
            dfs(i,path,total + sorted_arr[i])
            path.pop()
            dfs(i+1,path,total)
        
        dfs(0,[],0)
        return res
