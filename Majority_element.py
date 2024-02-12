class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        
        # Count occurrences of each element
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        # Check for the majority element
        for key in count:
            if count[key] > (n / 2):
                return key
        
        # If no majority element is found
        return -1
