class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        result=score=0
        tokens.sort()
        l,r=0,len(tokens)-1
        while l<=r:
            if power>=tokens[l]:
                power-=tokens[l]
                l+=1
                score+=1
                result=max(result,score)
            elif score>0:
                power+=tokens[r]
                score-=1
                r-=1
            else:
                break



        return result
