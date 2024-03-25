class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter=Counter(nums)
        return [num for num,count in counter.items() if count==2]
