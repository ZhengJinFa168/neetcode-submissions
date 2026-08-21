class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.get(nums[i]) == None:
                hashmap[nums[i]] = [i]
            else:
                hashmap[nums[i]].append(i)
        print(hashmap)
        for key, value in hashmap.items():
            complement = target - key
            if hashmap.get(complement) != None:
                print(value[0])
                first_num = value[0]
                if key == complement and len(value)>= 2:
                    return [first_num,value[1]]
                elif key == complement:
                    continue
                return [first_num,hashmap[complement][0]]
        
        return [0,0]

        
        