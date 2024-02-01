class Solution:
    def intToRoman(self, num: int) -> str:
        sym=['M','DM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman=''
        
        i=0
        while num>0 :
            while num>=value[i]:
                roman+=sym[i]
                num-=value[i]
            i+=1
        return roman

sol=Solution()
tryw=sol.intToRoman(1076)
print(tryw)
