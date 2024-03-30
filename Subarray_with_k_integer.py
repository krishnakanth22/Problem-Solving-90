class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res=0
        l_far=0
        l_near=0
        count=defaultdict(int)
        for r in range(len(nums)):
            count[nums[r]]+=1
            while len(count)>k:
                count[nums[l_near]]-=1
                if count[nums[l_near]]==0:
                    count.pop(nums[l_near])
                l_near+=1
                l_far=l_near
            while count[nums[l_near]]>1:
                count[nums[l_near]]-=1
                l_near+=1
            if len(count)==k:
                res+= l_near - l_far + 1
        return res
