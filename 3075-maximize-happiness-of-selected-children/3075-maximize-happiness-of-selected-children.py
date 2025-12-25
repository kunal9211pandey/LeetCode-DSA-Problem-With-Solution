class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)    

        total = 0
        decrease = 0

        for i in range(k):
            value = happiness[i] - decrease
            if value <= 0:
                break
            total += value
            decrease += 1

        return total