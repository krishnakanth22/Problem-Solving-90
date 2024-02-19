class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''for i in range (0,n):
            if (2**i == n):
                return True
        return False'''
        
        if n<=0:
            return False

        else:
            bit_id=bin(n).count("1")

        return bit_id==1
