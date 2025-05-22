class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        marker = 0.5
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for r in range(len(matrix)):
                        if matrix[r][j] != 0:
                            matrix[r][j] = marker
                    for c in range(len(matrix[0])):
                        if matrix[i][c] != 0:
                            matrix[i][c] = marker
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == marker:
                    matrix[i][j] = 0