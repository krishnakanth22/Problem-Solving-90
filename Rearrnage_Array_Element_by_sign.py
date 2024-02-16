class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        new_arr=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        for j in range(len(nums)):
            if j % 2 == 0:
                new_arr.append(pos.pop(0))  
            else:
                new_arr.append(neg.pop(0))  

        return new_arr
