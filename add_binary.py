class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string

    def addBinary(self, a, b):
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a

        carry = 0
        result = ''
        for index in reversed(xrange(len(a))):
            current = (int(a[index]) + int(b[index]) + carry) % 2
            carry = (int(a[index]) + int(b[index]) + carry) / 2
            result = str(current) + result
        if carry:
            result = str(carry) + result
        return result
