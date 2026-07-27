class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Frequency map of t
        f1 = {}
        for ch in t:
            f1[ch] = f1.get(ch, 0) + 1

        # Sliding window frequency
        f2 = {}

        have = 0
        need = len(f1)

        low = 0
        start = 0
        min_len = float("inf")

        for high in range(len(s)):
            ch = s[high]
            f2[ch] = f2.get(ch, 0) + 1

            # Character frequency matched
            if ch in f1 and f2[ch] == f1[ch]:
                have += 1

            # Shrink window while it is valid
            while have == need:
                window_len = high - low + 1

                if window_len < min_len:
                    min_len = window_len
                    start = low

                left_char = s[low]
                f2[left_char] -= 1

                if left_char in f1 and f2[left_char] < f1[left_char]:
                    have -= 1

                if f2[left_char] == 0:
                    del f2[left_char]

                low += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]