class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits

    def plusOne(self, digits):
        carry = 1
        for index in reversed(xrange(len(digits))):
            current = (digits[index] + carry) % 10
            carry = (digits[index] + carry) / 10
            digits[index] = current
        if carry:
            digits = [carry] + digits
        return digits
