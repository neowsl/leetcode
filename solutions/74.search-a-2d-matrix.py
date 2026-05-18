import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False

        row_mins = [xs[0] for xs in matrix]
        row = bisect.bisect_right(row_mins, target) - 1

        col = bisect.bisect_left(matrix[row], target)

        return col < len(matrix[0]) and matrix[row][col] == target
