class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first_strs=strs[0]
        last_strs=strs[-1]
        common_prefix=""
        for i in range (len(first_strs)):
            if i<len(last_strs) and first_strs[i]==last_strs[i]:
                common_prefix+=first_strs[i]
            else:
                break
        return common_prefix
       
