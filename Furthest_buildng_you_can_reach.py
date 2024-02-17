class Solution:
    def furthestBuilding(self, heights: List[int], b: int, l: int) -> int:
        n = len(heights)
        heap = []       
        for i in range(1, n):
            diff = heights[i] - heights[i - 1]            
            if diff > 0:
                heapq.heappush(heap, diff) 
                if len(heap) > l:
                    b -= heapq.heappop(heap)                  
                if b < 0:
                    return i - 1
        return n - 1  
