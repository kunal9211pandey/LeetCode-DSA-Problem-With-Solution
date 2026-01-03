class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j = 0
        for i in range(1,len(nums)):
                if nums[i] == nums[j]:
                    return True
                j += 1
        return False
        