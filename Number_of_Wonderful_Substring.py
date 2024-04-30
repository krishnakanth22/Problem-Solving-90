class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = 0
        n = len(word)
        prefix_counts = [0] * 1024  # 2^10 as there are 10 letters
        
        bitmask = 0
        prefix_counts[0] = 1
        
        for i in range(n):
            char_index = ord(word[i]) - ord('a')
            bitmask ^= 1 << char_index
            
            count += prefix_counts[bitmask]
            
            for j in range(10):
                count += prefix_counts[bitmask ^ (1 << j)]
            
            prefix_counts[bitmask] += 1
        
        return count
