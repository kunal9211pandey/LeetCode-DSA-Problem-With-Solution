class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        great = []
        equal = []
        
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                great.append(num)
            else:
                equal.append(num)
        return less + equal + great
        