class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1
        while (left_pointer < right_pointer):
            left_char = s[left_pointer]
            right_char = s[right_pointer]
            left_asci = ord(left_char.lower())
            right_asci = ord(right_char.lower())
            if not((left_asci>=48 and left_asci<=57) or (left_asci>=97 and left_asci <= 122)):
                left_pointer += 1
            if not((right_asci>=48 and right_asci<=57) or (right_asci>=97 and right_asci <= 122)):
                right_pointer -= 1
            if (((right_asci>=48 and right_asci<=57) or (right_asci>=97 and right_asci <= 122)) and ((left_asci>=48 and left_asci<=57) or (left_asci>=97 and left_asci <= 122))):
                if(right_asci != left_asci):
                    return False
                left_pointer += 1
                right_pointer -= 1
        return True