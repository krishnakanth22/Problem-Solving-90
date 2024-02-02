class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, l, r):
            if len(s) == 2 * n:
                result.append(s)
                return
            if l < n:
                backtrack(s + '(', l + 1, r)
            if r < l:
                backtrack(s + ')', l, r + 1)

        result = []
        backtrack('', 0, 0)
        return result
