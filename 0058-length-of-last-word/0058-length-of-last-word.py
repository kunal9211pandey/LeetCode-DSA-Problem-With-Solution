class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.strip().split()

        if not word:
            return 0
        return len(word[-1])