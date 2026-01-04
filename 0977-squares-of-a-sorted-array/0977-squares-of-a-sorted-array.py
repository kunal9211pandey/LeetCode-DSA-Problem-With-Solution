class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        index = n - 1

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                result[index] = left_square
                left += 1
            else:
                result[index] = right_square
                right -= 1

            index -= 1

        return result
