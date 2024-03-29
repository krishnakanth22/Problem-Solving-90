class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        count = 0
        left = 0
        max_count = 0
        
        for right in range(len(nums)):
            if nums[right] == max_num:
                max_count += 1
            
            while max_count >= k:
                count += len(nums) - right
                if nums[left] == max_num:
                    max_count -= 1
                left += 1

        return count
