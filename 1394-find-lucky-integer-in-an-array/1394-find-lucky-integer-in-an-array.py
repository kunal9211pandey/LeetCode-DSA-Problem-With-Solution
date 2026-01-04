class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        ans = -1
        for num in freq:
            if num == freq[num]:
                ans = max(ans, num)
        return ans
