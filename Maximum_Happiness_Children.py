class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        queue=[]
        for i in range(0,k):
            queue.append(max(happiness))
            happiness.remove(max(happiness))
            for j in range (len(happiness)):
                if happiness[j]>0:
                    happiness[j]-=1
