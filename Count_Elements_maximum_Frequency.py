class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_freq = max(counter.values())
        return sum(freq for freq in counter.values() if freq == max_freq)
