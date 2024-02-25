class Solution:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        n = len(nums)

        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                num1, num2 = nums[i], nums[j]
                if Solution.gcd(num1, num2) > 1:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            visited = [False] * n
            dfs(i)
            if not all(visited):
                return False

        return True
