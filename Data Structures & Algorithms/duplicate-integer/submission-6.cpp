class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> dict;
        int len = nums.size();
        int curr_number;
        cout << len;
        for(int i=0;i<len;i++){
            curr_number = nums[i];
            if (dict.count(curr_number) == 0){
                dict[curr_number] = 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};