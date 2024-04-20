class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(row, col):
            # If current cell is not farmland or already visited, return
            if row < 0 or row >= len(land) or col < 0 or col >= len(land[0]) or land[row][col] == 0:
                return
            # Mark current cell as visited
            land[row][col] = 0
            # Update the coordinates of the group
            farmland_group[2] = max(farmland_group[2], row)
            farmland_group[3] = max(farmland_group[3], col)
            # Recursively visit adjacent cells
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        groups = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    farmland_group = [i, j, i, j]  # Initialize group coordinates
                    dfs(i, j)
                    groups.append(farmland_group)
        
        return groups
