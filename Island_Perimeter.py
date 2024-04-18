class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0
            visit.add((i, j))
            p = 0
            p += dfs(i, j + 1)
            p += dfs(i, j - 1)
            p += dfs(i + 1, j)
            p += dfs(i - 1, j)
            return p
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    visit = set()
                    perimeter += dfs(i, j)
                    return perimeter
