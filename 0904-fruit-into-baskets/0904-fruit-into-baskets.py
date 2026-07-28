class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low = 0
        f = {}
        result = float("-inf")

        for high in range(len(fruits)):
            f[fruits[high]] = f.get(fruits[high], 0) + 1

            while len(f) > 2:
                f[fruits[low]] -= 1

                if f[fruits[low]] == 0:
                    del f[fruits[low]]

                low += 1

            length = high - low + 1
            result = max(result, length)

        return result