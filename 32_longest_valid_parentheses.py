class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        max_length = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.pop(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[0])

        return max_length
