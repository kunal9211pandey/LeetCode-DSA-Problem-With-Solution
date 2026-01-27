class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_one = 0
        final_one = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_one += 1
                final_one = max(final_one, current_one)
            else:
                current_one = 0
        return final_one
        