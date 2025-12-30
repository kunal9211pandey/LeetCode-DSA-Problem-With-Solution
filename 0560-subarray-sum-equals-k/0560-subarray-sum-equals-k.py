class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_subarray_count = 0
        current_prefix_sum = 0
        prefix_sum_frequency = {0: 1}

        for current_number in nums:
            current_prefix_sum += current_number

            if current_prefix_sum - k in prefix_sum_frequency:
                total_subarray_count += prefix_sum_frequency[current_prefix_sum - k]

            if current_prefix_sum in prefix_sum_frequency:
                prefix_sum_frequency[current_prefix_sum] += 1
            else:
                prefix_sum_frequency[current_prefix_sum] = 1

        return total_subarray_count
