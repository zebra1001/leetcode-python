class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        trailing_zeros = 0
        x = 1
        while n/x != 0:
            x = x * 5
            trailing_zeros += n/x
        return trailing_zeros