class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        start = 0
        result = []
        for i, char in enumerate(s):
            if char == '(':
                if balance == 0:
                    start = i  # Corrected typo from 'statr' to 'start'
                balance += 1
            elif char == ')':
                balance -= 1
                if balance == 0:
                    result.append(s[start + 1 : i])  # Extract inner content
        return "".join(result)