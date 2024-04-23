class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Construct adjacency list representation of the tree
        adj = [set() for i in range(n)]
        for s, d in edges:
            adj[s].add(d)
            adj[d].add(s)
        
        # Initialize a list of leaf nodes
        leaves_q = [i for i in range(n) if len(adj[i]) == 1]
        
        while n > 2:
            new_leaves = []
            for leaf in leaves_q:
                j = adj[leaf].pop()
                adj[j].remove(leaf)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            n -= len(leaves_q)
            leaves_q = new_leaves
        
        return leaves_q
