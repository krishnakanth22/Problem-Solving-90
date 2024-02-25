class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        parent = list(range(n))

        for i in range(n):
            for j in range(i + 1, n):
                if self.gcd(nums[i], nums[j]) > 1:
                    self.union(parent, i, j)

        root = self.find(parent, 0)
        for i in range(1, n):
            if self.find(parent, i) != root:
                return False

        return True

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def find(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, i, j):
        root_i = self.find(parent, i)
        root_j = self.find(parent, j)
        if root_i != root_j:
            parent[root_i] = root_j
