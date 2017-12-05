class Solution(object):
    # https://discuss.leetcode.com/topic/15295/seven-short-solutions-1-to-7-lines
    # beats 71.20%
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2):
            for j in range(n-n/2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                         matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

    def rotate1(self, A):
            A[:] = zip(*A[::-1])

    def rotate2(self, A):
        A[:] = map(list, zip(*A[::-1]))

    def rotate3(self, A):
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]

    def rotate4(self, A):
        n = len(A)
        for i in range(n / 2):
            for j in range(n - n / 2):
                for _ in '123':
                    A[i][j], A[~j][i], i, j = A[~j][i], A[i][j], ~j, ~i
                i = ~j

    def rotate5(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]

    def rotate6(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for row in A:
            for j in range(n / 2):
                row[j], row[~j] = row[~j], row[j]