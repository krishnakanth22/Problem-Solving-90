class Solution:
    def climbStairs(self, n: int) -> int:
        '''if n<=0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        else:
        
            return self.climbStairs(n-1) + self.climbStairs(n-2)'''
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
        
        '''a, b = 1, 2
        for i in range(n-1):
            a, b = b, a + b
        return a'''
