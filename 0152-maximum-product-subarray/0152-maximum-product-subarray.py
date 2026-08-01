class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = 0
        min_end = nums[0]
        max_end = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            v1 = min_end * nums[i]
            v2 = max_end * nums[i]
            v3 = nums[i]

            max_end = max(v3, max(v1, v2))
            min_end = min(v3, min(v1, v2))

            result = max(result, max(max_end, min_end))
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna