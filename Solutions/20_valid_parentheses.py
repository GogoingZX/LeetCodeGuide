# Python 3.x
# Stack
#
# ================================================================================

class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        left_num = 0
        right_num = 0
        brackets_stack = []
        
        for bracket in s:
            if bracket in brackets_map.keys():
                brackets_stack.append(bracket)
                left_num += 1
                
            elif bracket in brackets_map.values():
                right_num += 1
                try:
                    top = brackets_stack.pop()
                except:
                    return False
                
                if bracket == brackets_map[top]:
                    continue
                else:
                    return False
        
        if left_num != right_num:
            return False
        elif len(brackets_stack) != 0:
            return False
        else:
            return True

    
    def isValid_2(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack