class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        leng = len(nums)
        res = 0
        j = 0
        for i in range(0, leng):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            while freq[nums[i]] > k:
                freq[nums[j]] -= 1
                j += 1

            res = max(res, i - j + 1)

        return res
