class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        sum_k_nums = 0
        res = 0
        for r in range(len(arr)):
            sum_k_nums += arr[r]
            if (r-l)>=k:
                sum_k_nums -= arr[l]
                l += 1
            if (r-l)==k-1 and sum_k_nums / k >= threshold:
                res += 1
        
        return res
                