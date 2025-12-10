class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        poistive = []
        negative = []
         
        for num in nums:
            if num > 0:
                poistive.append(num)
            elif num < 0:
                negative.append(num)

        results = []   
        for i in range(len(poistive)):
            results.append(poistive[i])
            results.append(negative[i])
        return results
        