class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_letters_s={}
        for i in s:
            if seen_letters_s.get(i) == None:
                seen_letters_s[i] = 1
            else:
                seen_letters_s[i] += 1
        
        for i in t:
            if seen_letters_s.get(i) == None:
                return False
            else:
                seen_letters_s[i] -= 1
                
        for k,v in seen_letters_s.items():
            if v!=0:
                return False
        return True