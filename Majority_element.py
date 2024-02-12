class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for key in count:
            if count[key] > (n / 2):
                return key
        return -1
