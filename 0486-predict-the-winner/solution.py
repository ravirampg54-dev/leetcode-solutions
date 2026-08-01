class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # Base case: one element
        for i in range(n):
            dp[i][i] = nums[i]

        # Length of subarray
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                # Pick left or pick right
                dp[left][right] = max(
                    nums[left] - dp[left + 1][right],
                    nums[right] - dp[left][right - 1]
                )

        return dp[0][n - 1] >= 0
