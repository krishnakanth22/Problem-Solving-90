class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        track={}
        n=len(nums)
        for i in nums:
            track[i]=track.get(i,0)+1
        for key, value in track.items():
            if value==1:
                return key
