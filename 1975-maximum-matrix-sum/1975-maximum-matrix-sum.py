class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_abs = 0
        min_abs = float('inf')
        neg_count = 0
        has_zero = False
        
        for row in matrix:
            for x in row:
                total_abs += abs(x)
                min_abs = min(min_abs, abs(x))
                if x < 0:
                    neg_count += 1
                if x == 0:
                    has_zero = True
        
        return total_abs if has_zero or neg_count % 2 == 0 else total_abs - 2 * min_abs