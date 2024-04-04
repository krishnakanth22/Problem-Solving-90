class Solution:
    def maxDepth(self, s: str) -> int:
        output=0
        curr=0
        for i in s:
            if i=="(":
                curr+=1
            elif i==")":
                curr-=1
            output=max(output,curr)
        return output
