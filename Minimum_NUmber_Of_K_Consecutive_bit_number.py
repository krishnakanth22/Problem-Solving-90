class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        res=0
        flipped=0
        isFlipped=[0]*n
        for i in range(n):
            if i>=k:
                flipped^=isFlipped[i-k]
            if flipped==nums[i]:
                if i+k>n:
                    return -1
                isFlipped[i]=1
                flipped^=1
                res+=1
        return res
