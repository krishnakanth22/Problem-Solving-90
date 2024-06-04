class Solution:
    def longestPalindrome(self, s: str) -> int:
        res=0
        val=0
        track={}
        for i in s:
            track[i]=track.get(i,0)+1

        for count in track.values():
            if count%2!=0:
                res+=count-1
                val=1
            else:
                res+=count
        return res+val 
