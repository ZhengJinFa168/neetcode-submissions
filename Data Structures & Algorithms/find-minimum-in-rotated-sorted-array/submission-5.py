class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenght = len(nums)
        minimun = nums[lenght - 1]
        l = 0
        r = lenght - 1
        temp = 0
        while l<r:
            if nums[r] < minimun:
                minimun = nums[r]
            if nums[l]< minimun:
                minimun = nums[l]
            #print("r: " + str(r) +" l: "+ str(l))
            mid = math.ceil((r+l)/2)
            if nums[mid] < nums[r]:
                if nums[mid] < minimun:
                    minimun = nums[mid]
                r = mid - 1
            else:
                l = mid + 1

        return minimun