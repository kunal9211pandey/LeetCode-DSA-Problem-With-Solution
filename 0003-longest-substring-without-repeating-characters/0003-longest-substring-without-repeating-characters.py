class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        f = {}
        result = 0

        for high in range(len(s)):
            f[s[high]] = f.get(s[high], 0) + 1

            while f[s[high]] > 1:
                f[s[low]] -= 1
                if f[s[low]] == 0:
                    del f[s[low]]
                low += 1

            length = high - low + 1
            result = max(result, length)

        return result