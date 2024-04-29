class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char not in char_to_word and word not in word_to_char:
                char_to_word[char] = word
                word_to_char[word] = char
            elif char not in char_to_word or char_to_word[char] != word:
                return False

        return True
