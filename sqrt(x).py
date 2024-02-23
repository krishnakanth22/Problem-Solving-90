class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        i,j = 1, x
        result = 0

        while i <= j:
            mid = (i + j) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                i = mid + 1
                result = mid
            else:
                j = mid - 1
        return result
