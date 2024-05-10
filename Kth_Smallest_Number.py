class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        maxHeap = []      

        for i in range(n) :
            for j in range(i + 1, n) : 
                if len(maxHeap) < k :
                    heappush(maxHeap, (- arr[i] / arr[j], i, j))

                else :
                    heappushpop(maxHeap, (- arr[i] / arr[j], i, j))

        smallest, i, j = maxHeap[0]

        return (arr[i], arr[j])
