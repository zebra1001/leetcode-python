class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing

    def merge(self, A, m, B, n):
        indexA = m - 1
        indexB = n - 1
        while indexA >= 0 and indexB >= 0:
            if A[indexA] > B[indexB]:
                A[indexA + indexB + 1] = A[indexA]
                indexA -= 1
            else:
                A[indexA + indexB + 1] = B[indexB]
                indexB -= 1
        while indexB >= 0:
            A[indexB] = B[indexB]
            indexB -= 1

    def merge1(self, A, m, B, n):
        index_a = 0
        index_b = 0
        while index_a < m and index_b < n:
            if A[index_a] >= B[index_b]:
                A.insert(index_a, B[index_b])
                index_a += 1
                index_b += 1
            else:
                index_a += 1
        if index_b < n:
            A.extend(B[index_b::])
