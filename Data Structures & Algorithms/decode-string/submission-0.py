class Solution:
    def decodeString(self, s: str) -> str:
        stack = []      # Stores tuples of (prev_str, repeat_k)
        curr_str = ""
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                # Handle multi-digit numbers like "12[a]" -> 1 * 10 + 2 = 12
                curr_num = curr_num * 10 + int(char)
                
            elif char == "[":
                # Pause current state: push onto stack and reset for inner bracket
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
                
            elif char == "]":
                # Resume parent state: pop and attach repeated inner string
                prev_str, k = stack.pop()
                curr_str = prev_str + (curr_str * k)
                
            else:
                # Regular letter: add to current level's string
                curr_str += char
                
        return curr_str