class Solution:
    # @return a boolean

    def isPalindrome(self, x):
        if x < 0:
            return False
        length = 0
        tmp = x
        while tmp / 10 > 0:
            length += 1
            tmp = tmp / 10

        while length > 0:
            head = x / pow(10, length)
            tail = x % 10
            if head != tail:
                return False
            else:
                x = x % pow(10, length) / 10
                length -= 2

        return True

s = Solution()
print s.isPalindrome(9999)
