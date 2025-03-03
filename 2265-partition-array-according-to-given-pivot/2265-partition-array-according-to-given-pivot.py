class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        Less_than = []
        Equal_to = []
        Greater_than = []

        for num in nums:
            if num < pivot:
                Less_than.append(num)
            elif num == pivot:
                Equal_to.append(num)
            else:
                Greater_than.append(num)
        return Less_than + Equal_to + Greater_than