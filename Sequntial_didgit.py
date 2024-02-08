class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
    
        for i in range(1, 9):
            num = i
            next_digit = i
        
            while num <= high and next_digit < 10:
                if num >= low:
                    result.append(num)
            
                next_digit += 1
                num = num * 10 + next_digit
    
        return sorted(result)
