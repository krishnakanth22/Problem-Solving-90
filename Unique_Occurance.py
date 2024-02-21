class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        n = len(arr)
        for i in arr:
            count[i] = count.get(i, 0) + 1

        result=list(count.values())
        for j in range (1,len(result)):
            if result[j-1] == result[j]:
                return False
        return True
