class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        result=''
        for char in s:
            freq[char]=freq.get(char,0)+1
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        for i in range (len(freq)):
            result = ''.join(key * value for key, value in sorted_freq.items())
            return (result)
