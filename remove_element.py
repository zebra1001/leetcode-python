class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer

    def removeElement(self, A, elem):
        head = 0
        tail = len(A) - 1
        while head <= tail and head < len(A) and tail >= 0:
            if A[tail] == elem:
                tail -= 1
            if A[head] != elem:
                head += 1

            if head > tail or head >= len(A) or tail < 0:
                break

            if A[head] == elem and A[tail] != elem:
                temp = A[head]
                A[head] = A[tail]
                A[tail] = temp
                tail -= 1
                head += 1
        return tail + 1

s = Solution()
print s.removeElement([2], 2)
