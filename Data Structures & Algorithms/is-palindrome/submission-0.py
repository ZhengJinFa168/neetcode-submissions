class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = s.lower()
        no_spaces = ""
        for i in range(len(s)):
            lett=lowercase[i]
            asci=ord(lett)
            print(asci)
            if (asci>=48 and asci<=57) or (asci>=97 and asci <= 122):
                no_spaces = no_spaces + lowercase[i]
        
        full_lenght = len(no_spaces)
        lenght = (full_lenght + 2 - 1) // 2
        for i in range(int(lenght)):
            print(no_spaces[i])
            print(no_spaces[full_lenght-1-i])
            if no_spaces[i]!=no_spaces[full_lenght-1-i]:
                return False
            
        return True

        