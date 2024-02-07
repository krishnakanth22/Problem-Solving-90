class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        quotient = 0
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0  # Initialize result before the while loop

        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

            result = sign * quotient

        return max(min(result, INT_MAX), INT_MIN)
