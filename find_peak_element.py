class Solution:
    # @param num, a list of integer
    # @return an integer

    def findPeakElement(self, num):
        for index in xrange(len(num) - 1):
            if num[index] > num[index + 1]:
                return index

        return len(num) - 1


class Solution:
    # @param num, a list of integer
    # @return an integer

    def findPeakElement(self, num):
        return self.search(num, 0, len(num) - 1)

    def search(self, num, start, end):
        if start == end:
            return start
        if end - start == 1:
            return end if num[end] > num[start] else start
        mid = (start + end) / 2
        if num[mid] > num[mid - 1] and num[mid] > num[mid + 1]:
            return mid
        if num[mid] < num[mid - 1]:
            return self.search(num, start, mid - 1)
        else:
            return self.search(num, mid + 1, end)


s = Solution()
print s.findPeakElement([1, 2, 3, 4])
