class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        current_row = [1]
        for i in xrange(1, rowIndex + 1):
        	previous_row = current_row
        	current_row = [1]
        	for x in xrange(1, i):
        		current_row.append(previous_row[x] + previous_row[x - 1])
        	current_row.append(1)
        return current_row


    def getRow2(self, rowIndex):
        current_row = [1]
        for i in xrange(1, rowIndex + 1):
        	current_num = 1
        	for x in xrange(1, i):
        		prev_num = current_num
        		current_num = current_row[x]
        		current_row[x] = prev_num + current_num
        	current_row.append(1)
        return current_row


s = Solution()
print s.getRow2(5)
