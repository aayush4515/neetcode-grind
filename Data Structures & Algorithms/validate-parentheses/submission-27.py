class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']
        closed_brackets = [')', '}', ']']
        stack = []

        for char in s:
            if char in open_brackets:
                stack.append(char)
            
            if char in closed_brackets:
                if not stack:
                    return False
                curr_top = stack[-1]

                if char == ')' and curr_top == '(':
                    stack.pop()
                elif char == '}' and curr_top == '{':
                    stack.pop()
                elif char == ']' and curr_top == '[':
                    stack.pop()
                else:
                    stack.append(char)
            
        if not stack:
            return True
        return False
                


            
