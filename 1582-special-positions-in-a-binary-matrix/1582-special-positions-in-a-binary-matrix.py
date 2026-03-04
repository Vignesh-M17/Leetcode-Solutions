class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        col_counts = [0] * cols
        row_counts = [0] * rows
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    col_counts[j] += 1
                    row_counts[i] += 1
        
        count = 0
        for i in range(rows):  # Iterate over rows
            for j in range(cols):  # Iterate over columns
                if mat[i][j] == 1 and col_counts[j] == 1 and row_counts[i] == 1:
                    count += 1
        
        return count
        