class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        result = float('inf')
        sum_val = 0

        while high < len(nums):
            sum_val += nums[high]

            while sum_val >= target:
                length = high - low + 1
                result = min(result, length)
                sum_val -= nums[low]
                low += 1

            high += 1

        return 0 if result == float('inf') else result