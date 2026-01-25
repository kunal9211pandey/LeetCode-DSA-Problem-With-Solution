class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left = 0
            right = len(word) -1
            is_palindrome = True
            while left < right:
                if word[left] != word[right]:
                    is_palindrome = False
                left += 1
                right -=1
            if is_palindrome:
                return word
        return ""
        