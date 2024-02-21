class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = Counter(arr)
        seen = set()

        for count in occurrences.values():
            if count in seen:
                return False
            seen.add(count)

        return True
