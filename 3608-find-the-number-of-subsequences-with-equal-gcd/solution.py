from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAX = max(nums)

        # dp[g1][g2] = number of ways
        dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]
        dp[0][0] = 1

        for x in nums:
            new_dp = [row[:] for row in dp]

            for g1 in range(MAX + 1):
                for g2 in range(MAX + 1):
                    if dp[g1][g2] == 0:
                        continue

                    # Put x into first subsequence
                    ng1 = x if g1 == 0 else gcd(g1, x)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + dp[g1][g2]) % MOD

                    # Put x into second subsequence
                    ng2 = x if g2 == 0 else gcd(g2, x)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + dp[g1][g2]) % MOD

            dp = new_dp

        ans = 0
        for g in range(1, MAX + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans
