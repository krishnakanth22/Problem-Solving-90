class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        sign = 1
        if s and (s[0] == '+' or s[0] == '-'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        result = 0
        for i in s:
            if i.isdigit():
                result = result * 10 + int(i)
            else:
                break

        result *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        result = max(INT_MIN, min(result, INT_MAX))

        return result
