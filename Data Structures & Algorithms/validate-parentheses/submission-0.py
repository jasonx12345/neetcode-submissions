class Solution:
    def isValid(self, s: str) -> bool:

        #given a string given contains character s { } () []
        # its only a valid string if open braces have close brackets of the same type
        # open brackets must be closed in the correct order ({)} this is doesnt work as order is wrong
        # to start we must have a opening perentheses, we can add as many
        # as long as there is a closing canceling it out
        # we remove the top first one, we use a stack
        # and we use a hashmap to see if it of the closing matches opening
        stack = []
        close_to_open= {")" :"(","}" :"{","]" :"[" }

        for char in s:
            # Check if the current character is a closing bracket
            if char in close_to_open:
                # Verify the stack isn't empty and the top element matches the expected open bracket
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()  # Remove the matched opening bracket from the stack
                else:
                    return False  # Mismatched or unexpected closing bracket
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # Return True only if all opening brackets were properly closed (stack is empty)
        return not stack
        