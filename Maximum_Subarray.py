class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_arr=nums[0]
        curr=0
        for n in nums:
            if curr<0:
                curr=0
            curr+=n
            max_arr=max(max_arr,curr)
        return max_arr
