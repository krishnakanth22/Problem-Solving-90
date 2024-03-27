class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res=0
        l=0
        product=1
        for r in range (len(nums)):
            product*=nums[r]
            while product >=k and l<=r:
                product=product//nums[l]
                l+=1
            res+=(r-l+1)
        return res
