class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # Sort the array
        nums.sort()

        # Initialize the closest sum
        closest_sum = nums[0] + nums[1] + nums[2]
        min_diff = float('inf')

        # Fix one element
        for i in range(len(nums) - 2):

            # Two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:

                # Current triplet sum
                sum_val = nums[i] + nums[left] + nums[right]

                # Current difference from target
                diff = abs(sum_val - target)

                # Update closest sum if a smaller difference is found
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = sum_val

                # Exact target found
                if sum_val == target:
                    return sum_val

                # Need a larger sum
                elif sum_val < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return closest_sum