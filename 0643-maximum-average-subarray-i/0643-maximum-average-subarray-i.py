class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low = 0
        window_sum = 0
        result = float('-inf')

        for high in range(len(nums)):
            window_sum += nums[high]

            if high - low + 1 == k:
                result = max(result, window_sum / k)

                window_sum -= nums[low]
                low += 1

        return result