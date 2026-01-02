class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        j = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
            if i + 1 < len(nums) and nums[j] == nums[i + 1]:
                return nums[j]
            j += 1
        return nums[0]