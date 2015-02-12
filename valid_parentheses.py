class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
        	if c in ('(', '[', '{'):
        		stack.append(c)
        	else:
        		if not stack:
        			return False
        		top = stack.pop()
        		if top + c == '()' or top + c == '[]' or top + c == '{}':
        			continue
        		else:
        			return False

        if not stack:
        	return True
        else:
        	return False

    def isValid2(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for c in s:
        	if c not in pairs:
        		stack.append(c)
        	else:
        		if not stack:
        			return False
        		top = stack.pop()
        		if top == pairs[c]:
        			continue
        		else:
        			return False

        if not stack:
        	return True
        else:
        	return False

s = Solution()
print s.isValid('()[]{[()]}')