class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sorted_arr = sorted(nums)
        def dfs(i, path, total):
            if total == target:
                res.append(path[:])
                return
            
            for j in range(i,len(sorted_arr)):
                if total + sorted_arr[j]>target:
                    return
                path.append(sorted_arr[j])
                dfs(j,path,total + sorted_arr[j])
                path.pop()
        
        dfs(0,[],0)
        return res