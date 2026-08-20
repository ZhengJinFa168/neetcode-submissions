class Solution {
public:
    bool isAnagram(string s, string t) {
        int len_first = s.size();
        int len_second = t.size();
        if(len_first!=len_second){
            return false;
        }
        std::unordered_map<char, int> helper;
        for(int i=0;i<len_first;i++){
            helper[s[i]] += 1;
            helper[t[i]] -= 1; 
        }
        for(auto in : helper){
            if(in.second!=0){
                return false;
            }
        }
        return true;
    }
};
