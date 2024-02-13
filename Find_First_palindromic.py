class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        s=0
        while s < len(words):
            if words[s] == words[s][::-1]:
                return words[s]
            else:
                s+=1
        return ""
