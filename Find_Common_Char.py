class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = Counter(words[0])
        for word in words[1:]:
            word_freq=Counter(word)
            for char in min_freq:
                if char in word_freq:
                    min_freq[char]=min(min_freq[char],word_freq[char])
                else:
                    min_freq[char]=0

        result=[]
        for char,freq in min_freq.items():
            result.extend(char*freq) 
        return result
