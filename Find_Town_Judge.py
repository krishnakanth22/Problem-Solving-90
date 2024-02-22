class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        track = [0] * (n + 1)  
        for a, b in trust:
            track[b] += 1
        for i in range(1, n + 1):
            if track[i] == n-1 or track[i]==n:
                return i
        return -1
        '''
        """
        result=[]
        for a,b in trust:
            result.append(b)
        if n=2:
            return b
        else:
            for i in range 
        """

        track = [0] * (n + 1)   
        for a, b in trust:
            track[a] -= 1
            track[b] += 1
    
        for i in range(1, n + 1):
            if track[i] == n - 1:
                return i
    
        return -1
