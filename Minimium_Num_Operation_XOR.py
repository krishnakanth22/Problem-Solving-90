class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor^=num

        return bin(xor^k)[2:].count('1')
