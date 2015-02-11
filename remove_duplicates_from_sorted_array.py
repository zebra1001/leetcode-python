class Solution:
    # @param a list of integers
    # @return an integer

    def removeDuplicates(self, A):
        if not A:
            return 0
        slow = 0
        for fast in xrange(len(A)):
            if A[fast] == A[slow]:
                continue
            else:
                slow += 1
                A[slow] = A[fast]
        return slow + 1

s = Solution()
print s.removeDuplicates([1, 1, 2])
