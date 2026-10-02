class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,path,total):
            if total == target:
                res.append(path[:])
                return
            
            if total > target or i == len(candidates):
                return
            path.append(candidates[i])
            dfs(i+1,path,candidates[i] + total)  
            path.pop()

            while(i + 1 < len(candidates) and candidates[i]==candidates[1+i]):
                i+=1
            dfs(i+1,path,total)

        dfs(0,[],0)
        return res