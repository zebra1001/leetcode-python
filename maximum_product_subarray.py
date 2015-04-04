class Solution:
    # @param A, a list of integers
    # @return an integer

    def maxProduct(self, A):
        if not A:
            return 0

        maximum = A[0]
        minimum = A[0]
        result = A[0]

        for i in A[1::]:
            temp = maximum
            maximum = max(max(maximum * i, minimum * i), i)
            minimum = min(min(temp * i, minimum * i), i)
            result = max(maximum, result)

        return result
