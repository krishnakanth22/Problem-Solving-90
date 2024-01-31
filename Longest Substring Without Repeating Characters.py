class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # Map to store the index of each character
        start = max_length = 0  # Start index of the current substring and maximum length

        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                # If the character is repeated and its last occurrence is within the current substring
                start = char_index_map[char] + 1  # Move the start index to the next position after the last occurrence

            char_index_map[char] = end
            max_length = max(max_length, end - start + 1)  

        return max_length
