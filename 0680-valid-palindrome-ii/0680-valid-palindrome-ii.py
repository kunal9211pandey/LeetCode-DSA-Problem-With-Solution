class Solution:
    def validPalindrome(self, s: str) -> bool:

        def ispalindrome(left , right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return ispalindrome(i + 1 ,j) or ispalindrome(i , j-1)
            i += 1
            j -= 1
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna