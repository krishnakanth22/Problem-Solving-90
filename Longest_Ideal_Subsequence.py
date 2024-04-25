class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*26
        for c in s:
            curr=ord(c)-ord('a')
            longest=1
            for prev in range (26):
                if abs(curr-prev)<=k:
                    longest=max(longest,1+dp[prev])
            dp[curr]=max(dp[curr],longest)
        return max(dp)
            
