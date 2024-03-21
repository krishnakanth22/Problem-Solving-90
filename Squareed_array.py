class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
            sqr=i**2
            result.append(sqr)
        result=sorted(result)
        return result
