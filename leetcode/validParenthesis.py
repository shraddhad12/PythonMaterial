class Solution(object):
    def isValid(self, s):
        brackets = dict(('()', '[]', '{}'))
        print(brackets)
        stack = []
        for i in s:
            # If open parentheses are present, append it to stack...
            if i in '([{':
                stack.append(i)
            elif len(stack) == 0 or i != brackets[stack.pop()]:
                return False
        return len(stack) == 0
    
s = "u{[]}"
print(Solution().isValid(s))