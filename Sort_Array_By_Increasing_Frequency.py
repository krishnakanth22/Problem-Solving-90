class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        track = Counter(nums)

        sorted_items = sorted(track.items(), key=lambda item: (item[1], -item[0]))
        
        result = []
        for key, freq in sorted_items:
            result.extend([key] * freq)
        
        return result
