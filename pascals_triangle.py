class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	result = []
    	if numRows == 0:
    		return []
    	result.append([1])
        for n in xrange(1, numRows):
        	r = [1]
        	for i in xrange(1, n):
        		r.append(result[n - 1][i - 1]+result[n - 1][i])
        	r.append(1)
        	result.append(r)
        return result

s = Solution()
print s.generate(5)