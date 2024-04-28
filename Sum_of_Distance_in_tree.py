class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        count = [1] * n
        sum_distances = [0] * n
        def dfs(node, parent):
            for neighbor in adj_list[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    count[node] += count[neighbor]
                    sum_distances[node] += sum_distances[neighbor] + count[neighbor]
        def propagate(node, parent):
            for neighbor in adj_list[node]:
                if neighbor != parent:
                    sum_distances[neighbor] = sum_distances[node] - count[neighbor] + (n - count[neighbor])
                    propagate(neighbor, node)
        dfs(0, -1)
        propagate(0, -1)
        return sum_distances
