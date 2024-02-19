class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = format(n, "032b")
        reversed_str = ''.join(reversed(binary_str))
        number = int(reversed_str, 2)
        return number
