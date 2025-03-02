class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        merge_array = []
        while first < len(nums1) or second < len(nums2):
            if first >= len(nums1):
                merge_array.append(nums2[second])
                second += 1
                continue
            elif second >= len(nums2):
                merge_array.append(nums1[first])
                first += 1
                continue

            if nums1[first][0] == nums2[second][0]:
                value = nums1[first][1] + nums2[second][1]
                merge_array.append([nums1[first][0], value])
                first += 1
                second += 1
                continue
                
            if nums1[first][0] < nums2[second][0]:
                merge_array.append(nums1[first])
                first += 1
            else:
                merge_array.append(nums2[second])
                second += 1
        return merge_array 