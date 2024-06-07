class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        words = sentence.split()
        
        for i in range(len(words)):
            for j in range(1, len(words[i])):
                if words[i][:j] in roots:
                    words[i] = words[i][:j]
                    break
        
        return ' '.join(words)
