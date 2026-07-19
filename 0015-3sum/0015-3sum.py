class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # Sort the array to apply the two-pointer approach
        nums.sort()

        # Store all unique triplets
        result = []

        # Fix one element at a time
        for i in range(0, len(nums) - 2):

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers
            left = i + 1
            right = len(nums) - 1

            # Target value that left + right should equal
            sum_val = -nums[i]

            # Find two numbers whose sum equals the target
            while left < right:

                s = nums[left] + nums[right]

                # Triplet found
                if s == sum_val:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate values from the left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values from the right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Increase sum by moving the left pointer
                elif s < sum_val:
                    left += 1

                # Decrease sum by moving the right pointer
                else:
                    right -= 1

        # Return all unique triplets
        return result