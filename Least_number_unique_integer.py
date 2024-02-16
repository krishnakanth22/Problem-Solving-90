class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        track={}
        
        for i in arr:
            track[i]=track.get(i,0)+1

        sorted_k = sorted(track.values())

        unique=len(sorted_k)
        for num in sorted_k:
            if num <= k:
                k-= num
                unique-= 1
            else:
                break
        return unique
