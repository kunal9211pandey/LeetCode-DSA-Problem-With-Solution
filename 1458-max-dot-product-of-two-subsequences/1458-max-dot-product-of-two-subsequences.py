class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        # dp[i][j] = maximum dot product using subsequences
        # ending at nums1[i-1] and nums2[j-1]
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                product = nums1[i-1] * nums2[j-1]

                dp[i][j] = max(
                    product,                    # start new subsequence
                    dp[i-1][j-1] + product,     # extend existing subsequence
                    dp[i-1][j],                 # skip nums1 element
                    dp[i][j-1]                  # skip nums2 element
                )

        return dp[n][m]
