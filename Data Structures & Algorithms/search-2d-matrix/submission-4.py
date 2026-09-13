class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_el = len(matrix) * len(matrix[0])

        if total_el == 1 and matrix[0][0] == target:
            return True
        elif total_el == 1 and matrix[0][0] != target:
            return False

        right = total_el - 1
        left = 0

        cur_idx = total_el // 2

        while left <= right:
            cur_outer = cur_idx // len(matrix[0])
            cur_inner = cur_idx % len(matrix[0])

            cur = matrix[cur_outer][cur_inner]

            if cur == target:
                return True
            
            elif cur < target:
                left = cur_idx + 1
            
            elif cur > target:
                right = cur_idx - 1
            
            cur_idx = (left + right) // 2
        
        return False



        