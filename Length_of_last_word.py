class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result=s.split()
        return len(result[-1])

        '''k=[]
        k=s.split(" ")
        l=" "
        ans=0
        for i in k:
            if i  not in l:
                ans=len(i)
        return ans'''
        
