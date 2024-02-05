class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
haystack = "hello"
needle = "ll"

result = strStr(haystack, needle)
print(result)  # Output: 2
