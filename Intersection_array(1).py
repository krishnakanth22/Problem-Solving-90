from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = len(nums1)
        len2 = len(nums2)
        result = []
        if len1 > len2:
            i = 0
            while i < len(nums2):
                j = 0
                while j < len(nums1):
                    if nums2[i] == nums1[j]:
                        result.append(nums2[i])
                        break
                    j += 1
                i += 1
        else:
            i = 0
            while i < len(nums1):
                j = 0
                while j < len(nums2):
                    if nums1[i] == nums2[j]:
                        result.append(nums1[i])
                        break
                    j += 1
                i += 1
        return result
