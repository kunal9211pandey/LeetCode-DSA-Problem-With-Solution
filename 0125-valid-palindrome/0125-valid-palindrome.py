class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert all upper to lower case
        s = s.lower()

        # keep only alphanumeric char
        s = "".join(ch for ch in s if ch.isalnum())

        i = 0
        j = len(s)-1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna