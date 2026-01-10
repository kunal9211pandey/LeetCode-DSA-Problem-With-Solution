class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        length_s1 = len(s1)
        length_s2 = len(s2)

        # dp[i][j] = minimum ASCII sum to make s1[i:] and s2[j:] equal
        dp = [[0] * (length_s2 + 1) for _ in range(length_s1 + 1)]

        # Base case: delete all remaining characters
        for i in range(length_s1 - 1, -1, -1):
            dp[i][length_s2] = dp[i + 1][length_s2] + ord(s1[i])

        for j in range(length_s2 - 1, -1, -1):
            dp[length_s1][j] = dp[length_s1][j + 1] + ord(s2[j])

        # Fill DP table
        for i in range(length_s1 - 1, -1, -1):
            for j in range(length_s2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    delete_from_s1 = ord(s1[i]) + dp[i + 1][j]
                    delete_from_s2 = ord(s2[j]) + dp[i][j + 1]
                    dp[i][j] = min(delete_from_s1, delete_from_s2)

        return dp[0][0]
