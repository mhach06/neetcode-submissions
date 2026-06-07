class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = []
        counter = 0

        brackets = {')': '(', ']': '[', '}': '{'}
        
        while counter < len(s):
            current_element = s[counter]

            if current_element in brackets:
                if not stack or stack[-1] != brackets[current_element]:
                    return False
                
                stack.pop()
            else:
                stack.append(current_element)
            
            counter += 1
        
        return len(stack) == 0

        
        