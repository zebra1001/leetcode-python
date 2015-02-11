class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
    	number = 0
    	for i, c in enumerate(s[::-1]):
    		number += pow(26, i) * (ord(c) - ord('A') + 1)
    	return number