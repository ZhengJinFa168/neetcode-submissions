class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1

        sorted_dict = dict(sorted(hashmap.items(), key=lambda x: x[1],reverse=True ))

        i=0
        output = []
        for key,v in sorted_dict.items():
            if i>=k:
                break
            output.append(key)
            i+=1
        return output
            

        