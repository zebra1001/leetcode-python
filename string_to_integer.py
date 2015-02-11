class Solution:
    # @return an integer

    def atoi(self, str):
        sol = 0
        sign = 1
        start_convert = False
        for c in str:
            if c.isspace() and not start_convert:
                continue
            elif c == '-' and not start_convert:
                sign = -1
                start_convert = True
            elif c == '+' and not start_convert:
                sign = 1
                start_convert = True
            elif c.isdigit():
                if not start_convert:
                    start_convert = True
                if sol > 214748364 or (sol == 214748364 and int(c) >= 8):
                    if sign == 1:
                        return 2147483647
                    else:
                        return -2147483648
                sol = sol * 10 + int(c)
            else:
                if not start_convert:
                    return 0
                else:
                    return sol * sign

        return sol * sign

s = Solution()
print s.atoi('-2147483647')
