class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen_letters_s={}
        for i in range(len(s)):
            if seen_letters_s.get(ord(s[i])) == None:
                seen_letters_s[ord(s[i])] = 1
            else:
                seen_letters_s[ord(s[i])] += 1
            if seen_letters_s.get(ord(t[i])) == None:
                seen_letters_s[ord(t[i])] = -1
            else:
                seen_letters_s[ord(t[i])] -= 1
        for k,v in seen_letters_s.items():
            if v!=0:
                return False
        return True