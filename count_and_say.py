class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for i in xrange(n-1):
            prev = next = ''
            num = 0
            for curr in s:
                if prev != '' and prev != curr:
                    next += str(num) + prev
                    num = 1
                else:
                    num += 1
                prev = curr
            next += str(num) + prev
            s = next
        return s