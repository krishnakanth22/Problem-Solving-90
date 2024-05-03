class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        max_len = max(len(ver1), len(ver2))
        
        for i in range(max_len):
            n1 = 0 if i >= len(ver1) else int(ver1[i])
            n2 = 0 if i >= len(ver2) else int(ver2[i])
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        
        return 0
