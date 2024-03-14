class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_count = {0: 1}  # Dictionary to store prefix sums and their frequencies
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            if current_sum - goal in prefix_sum_count:
                count += prefix_sum_count[current_sum - goal]
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
        
        return count
