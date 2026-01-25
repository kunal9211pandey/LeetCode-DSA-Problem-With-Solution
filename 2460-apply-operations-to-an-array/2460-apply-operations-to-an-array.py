class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: move zeros to the end (stable)
        write = 0
        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        while write < n:
            nums[write] = 0
            write += 1

        return nums
