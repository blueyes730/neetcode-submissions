class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []

        i, j, len1, len2 = 0, 0, len(nums1), len(nums2)
        combined_len = len1 + len2

        while i < len1 and j< len2:
            curr1 = nums1[i]
            curr2 = nums2[j]

            if curr1 < curr2:
                merged.append(curr1)
                i += 1
            else:
                merged.append(curr2)
                j += 1
        
        while i < len1:
            merged.append(nums1[i])
            i += 1
        while j < len2:
            merged.append(nums2[j])
            j += 1

        mid = combined_len // 2
        print(f"merged: {merged}")
        print(mid)
        if combined_len % 2 == 0:
            mid = combined_len//2
            return (float(merged[mid]) + float(merged[mid - 1])) / 2.0
        
        else:
            return float(merged[mid])