class Solution:
    def pivotInteger(self, n: int) -> int:
        first = sum([i for i in range(n+1)])
        second,x = n,n

        while x:
            if first==second:
                return x
            first-=x
            second+=x-1
            x-=1

        return -1
