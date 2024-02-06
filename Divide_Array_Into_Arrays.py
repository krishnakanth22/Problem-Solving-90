class Solution:
  def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    ans = []

    nums.sort()

    for i in range(2, len(nums), 3):
        if nums[i] - nums[i - 2] <= k:
            ans.append([nums[i - 2], nums[i - 1], nums[i]])
        else:
            return []
    

    return ans
