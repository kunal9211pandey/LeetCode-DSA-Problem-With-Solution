class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numbers_set = set(nums)
        longest_streak = 0

        for number in numbers_set:
            # start of a sequence
            if number - 1 not in numbers_set:
                current_number = number
                current_streak = 1

                while current_number + 1 in numbers_set:
                    current_number += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
