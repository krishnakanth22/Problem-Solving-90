class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        '''queue=[]
        for i in range(0,k):
            queue.append(max(happiness))
            happiness.remove(max(happiness))
            for j in range (len(happiness)):
                if happiness[j]>0:
                    happiness[j]-=1
        return sum(queue)'''
        """happiness.sort()
        selected=happiness[-k:]
        for i in range(k):
            selected[i]=max(selected[i]-i,0)
        return sum(selected)"""
        n = len(happiness)
        happiness.sort(reverse=True)  
        total_happiness = 0
        for i in range(min(k, n)):  
            total_happiness += max(happiness[i] - i, 0)  
        return total_happiness

