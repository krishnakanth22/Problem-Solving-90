class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in digits:
            num=num*10+i
        num=num+1
        
        result = [int(digit) for digit in str(num)]
        return result 



