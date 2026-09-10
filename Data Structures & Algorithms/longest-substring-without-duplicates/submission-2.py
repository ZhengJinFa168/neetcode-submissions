class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        i = 2
        lenght = len(s)
        hashtable = {}
        l = 0
        r = 1
        hashtable[s[l]] = 1
        temp, res = 1, 1
        if not hashtable.get(s[r],0):     
            hashtable[s[r]] = 1
            temp, res = 2, 2

        while i < lenght:
            #print("current window before changes: " + s[l:i+1])
            if not hashtable.get(s[i],0):
                hashtable[s[i]] = 1
                r += 1
                temp += 1
                #print("increasing window size with temp: " + str(temp))
                if temp > res:
                    res = temp
            else:
                if s[i] == s[r]:
                    temp = 1
                    hashtable = {}
                    hashtable[s[i]] = 1
                    r = i
                    l = i
                else:
                    hashtable[s[i]] += 1
                    hashtable[s[l]] -= 1
                    l += 1
                    #print("decreasing window size with temp: " + str(temp))
                    #print("l: " + str(l))
                    while hashtable[s[i]] > 1:
                        #print("ciao")
                        temp -= 1
                        hashtable[s[l]] -= 1
                        l += 1                  
            i += 1
        return res
        
        