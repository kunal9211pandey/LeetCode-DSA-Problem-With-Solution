class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2 == 1:
                j -= 1

        return nums
