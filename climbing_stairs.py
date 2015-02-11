class Solution:
    # @param n, an integer
    # @return an integer
    
    def climbStairs(self, n):
    	step = [0] * (n + 1)
    	step[1] = 1
    	if n == 1:
    	    return step[1]
    	step[2] = 2
    	if n <= 2:
    		return step[n]

    	for index in xrange(3, n+1):
    		step[index] = step[index-1] + step[index-2]

    	return step[n]


   	def climbStairs(self, n):
   		# Time limit exceeds!!!
    	if n < 0:
    		return 0
        elif n == 0:
        	return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)