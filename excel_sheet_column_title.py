class Solution:
    # @return a string
    def convertToTitle(self, num):
    	string = ''
    	while num > 0:
    		string = chr(ord('A') + (num-1)%26) + string
    		num = (num-1) / 26
    	return string