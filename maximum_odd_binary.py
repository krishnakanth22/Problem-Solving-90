class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_ones = s.count('1')
        n=len(s)
        if count_ones == 1:
            return ('0'*(n-1) + '1')

        result = '1'* (count_ones-1) + '0' * (n-count_ones) + '1' 
        
        return result
