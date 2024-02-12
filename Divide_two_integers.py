class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        return min(max(sign * quotient, -2**31), 2**31 - 1)
