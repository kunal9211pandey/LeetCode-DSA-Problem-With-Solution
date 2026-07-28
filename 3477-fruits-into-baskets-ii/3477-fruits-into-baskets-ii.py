class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]):
        used = [False] * len(baskets)
        count = 0

        i = 0

        while i < len(fruits):
            j = 0
            placed = False

            while j < len(baskets):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True
                    placed = True
                    break
                j += 1

            if not placed:
                count += 1

            i += 1

        return count