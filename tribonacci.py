class Solution:
    def tribonacci(self, n: int) -> int:
        """if n <= 0:
            return n
        if n == 1 or n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)"""
        a=0
        b=1
        c=1
        if n<=0:
            return n
        if n==1 or n==2:
            return 1
        else:
            for i in range(3,n+1):     
                d=a+b+c
                a=b
                b=c
                c=d
            return d
