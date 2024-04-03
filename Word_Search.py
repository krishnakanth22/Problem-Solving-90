class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(i, j, ind):
            if ind == len(word):
                return True
            if i < 0 or i >= row or j < 0 or j >= col or visited[i][j] or board[i][j] != word[ind]:
                return False
            visited[i][j] = True
            if (solve(i+1, j, ind+1) or
                solve(i-1, j, ind+1) or
                solve(i, j+1, ind+1) or
                solve(i, j-1, ind+1)):
                return True
            visited[i][j] = False
            return False
        
        row, col = len(board), len(board[0])
        visited = [[False] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if solve(i, j, 0):
                    return True
        return False
