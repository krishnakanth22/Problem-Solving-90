class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        queue = deque([('0000', 0)])
        visited = set(['0000'])
        
        while queue:
            current, moves = queue.popleft()
            if current == target:
                return moves
            if current in deadends:
                continue
            for i in range(4):
                for j in [-1, 1]:
                    new_digit = (int(current[i]) + j) % 10
                    new_combo = current[:i] + str(new_digit) + current[i+1:]
                    if new_combo not in visited and new_combo not in deadends:
                        visited.add(new_combo)
                        queue.append((new_combo, moves + 1))
        
        return -1
