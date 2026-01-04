class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Three pointers
        i = m - 1          # last valid index in nums1
        j = n - 1          # last index in nums2
        k = m + n - 1      # last index of nums1 (total space)

        # Merge from right to left
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
