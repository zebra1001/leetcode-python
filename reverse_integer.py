class Solution:
    # @return an integer

    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        sol = 0
        while x != 0:
            if sol > 214748364 or (sol == 214748364 and x % 10 >= 8 and sign == 1) or (sol == 214748364 and x % 10 > 8 and sign == -1):
                return 0
            sol = sol * 10 + x % 10
            x = x / 10
        sol = sign * sol
        return sol


s = Solution()
print s.reverse(1534236469)
