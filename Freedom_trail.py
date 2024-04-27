class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}

        def dp(index, pos):
            if index == len(key):
                return 0

            if (index, pos) in memo:
                return memo[(index, pos)]

            result = float('inf')
            for i in range(len(ring)):
                if ring[i] == key[index]:
                    clockwise = (pos - i) % len(ring)
                    anticlockwise = (i - pos) % len(ring)
                    steps = min(clockwise, anticlockwise) + 1
                    steps += dp(index + 1, i)
                    result = min(result, steps)

            memo[(index, pos)] = result
            return result

        return dp(0, 0)
