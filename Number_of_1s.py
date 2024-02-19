class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_str = format(n, '032b')  # Ensure the binary string is 32 bits long
        '''one_count = 0
        for bit in binary_str:
            if bit == '1':
                one_count += 1
        return one_count'''
        return binary_str.count("1")
