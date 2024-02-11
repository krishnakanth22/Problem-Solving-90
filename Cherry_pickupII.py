class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]
        def dp(row, col1, col2):
            if memo[row][col1][col2] != -1:
                return memo[row][col1][col2]
            if row == rows - 1:
                return grid[row][col1] if col1 == col2 else grid[row][col1] + grid[row][col2]
            result = 0
            for move1 in range(-1, 2):
                for move2 in range(-1, 2):
                    new_col1, new_col2 = col1 + move1, col2 + move2
                    if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                        result = max(result, dp(row + 1, new_col1, new_col2))
            result += grid[row][col1] if col1 == col2 else grid[row][col1] + grid[row][col2]
            memo[row][col1][col2] = result
            return result
        return dp(0, 0, cols - 1)


