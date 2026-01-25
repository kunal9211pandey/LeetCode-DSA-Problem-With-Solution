class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = list(s)
        n = len(word_list)
        start = 0

        for i in range(n + 1):
            if i == n or word_list[i] == ' ':
                left = start
                right = i - 1

                while left < right:
                    word_list[left], word_list[right] = word_list[right], word_list[left]
                    left += 1
                    right -= 1

                start = i + 1

        return "".join(word_list)
