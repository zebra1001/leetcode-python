class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
    	count = {}
    	for n in num:
    		if n not in count.keys():
    			count[n] = 1
    		else:
    			count[n] += 1
    		if count[n] > n/2:
    			return n

    def majorityElement2(self, num):
    	num = num.sort()
    	return num[len(num)/2]

    def majorityElement3(self, num):
    	candidate = None
    	count = 0
    	for n in num:
    		if count == 0:
    			candidate = n
    			count = 1
    		else:
    			if n == candidate:
    				count += 1
    			else:
    				count -= 1
    	return candidate
