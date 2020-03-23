class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        r = 0
        if target < matrix[0][0] or target > matrix[row-1][col-1]:
            return False
        for i in range(row):
            if matrix[i][0] <= target and matrix[i][col-1] >= target:
                r = i
                break
            if i == row-1:
                return False
        left = 0
        right = col -1
         
        while left <= right:
            mid = int((left+right)/2)
            if matrix[r][mid] > target:
                right = mid-1
            elif matrix[r][mid] < target:
                left = mid+1
            elif matrix[r][mid] == target:
                return True
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        #二分查找
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False

