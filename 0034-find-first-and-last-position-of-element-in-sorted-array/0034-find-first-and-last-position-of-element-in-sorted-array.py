class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        frist_index = -1
        last_index = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                frist_index = mid
                right = mid - 1
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2

            if nums[mid] == target:
                last_index = mid
                left = mid + 1
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

         
        return [frist_index , last_index]