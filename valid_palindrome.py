class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        import re
        s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
        for index in xrange(0, len(s)/2):
        	if s[index] != s[len(s) - index -1]:
        		return False
        return True

    def isPalindrome2(self, s):
        head = 0
        tail = len(s) - 1
        while head < len(s)/2 and tail >= len(s)/2:
        	if not s[head].isalnum():
        		head += 1
        	if not s[tail].isalnum():
        		tail -=1

        	if s[head].isalnum() and s[tail].isalnum():
        		if s[head].lower() != s[tail].lower():
        			return False
	        	else:
	        		head += 1
	        		tail -=1

        return True