class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)

        i=0
        j=n-1
        while i<j and s[i]==s[j]:
            while i<j and s[i]==s[i+1]:
                i+=1
            while i<=j and s[j]==s[j-1]:
                j-=1
            i+=1
            j-=1
        return max(0,j-i+1)
