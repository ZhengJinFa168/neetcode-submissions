class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, array<int, 2>> hashmap;
        int len = nums.size();
        for(int i=0;i<len;i++){
            if(hashmap.contains(nums[i])){
                if(hashmap[nums[i]][1]==0)
                    hashmap[nums[i]][1]= i;
            }else{
                hashmap[nums[i]]={i,0};
            }
        }
        int complement;
        for (auto it = hashmap.begin(); it != hashmap.end(); ++it) {
            complement = target - it->first;
            if(it->first == complement){
                if((it->second)[1]!=0){
                    return {(it->second)[0],(it->second)[1]};
                }
            }
            if(hashmap.contains(complement)){
                if ((it->second)[0]<hashmap[complement][0]){
                    return {(it->second)[0],hashmap[complement][0]};
                }else{
                    return {hashmap[complement][0],(it->second)[0]};
                }
            }
        }
        return {0,0};
    }
};
