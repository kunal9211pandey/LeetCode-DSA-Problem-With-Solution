class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_strick = 0

        for num in num_set:
            if num - 1 not in num_set: # frist element
                current_num = num
                current_strick = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_strick += 1
                longest_strick = max(current_strick , longest_strick) 
        return longest_strick


