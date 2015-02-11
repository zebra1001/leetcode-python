class Solution:
    # @param num, a list of integers
    # @return a string

    def largestNumber(self, num):
        comp = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
        num = map(str, num)
        num.sort(cmp=comp, reverse=True)
        return str(int("".join(num)))

s = Solution()
print s.largestNumber([3, 30, 34, 5, 9])
