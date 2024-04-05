class Solution:
    def makeGood(self, s: str) -> str:
        res = s  # Initialize res with the input string
        i = 0
        while i < len(res) - 1:  # Iterate through the string
            if res[i].lower() == res[i + 1].lower() and res[i] != res[i + 1]:
                # If current character and next character form a pair of the same letter but different cases
                # Remove the pair by updating res
                res = res[:i] + res[i + 2:]
                i = max(0, i - 1)  # Move back one step to recheck previous characters
            else:
                i += 1  # Move to the next character
        return res
