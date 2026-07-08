from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        n = len(digits)

        # prefix digit sum
        prefix_sum = [0] * (n + 1)

        # prefix number
        prefix_num = [0] * (n + 1)

        # powers of 10
        pow10 = [1] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = (prefix_sum[i] + digits[i]) % MOD
            prefix_num[i + 1] = (prefix_num[i] * 10 + digits[i]) % MOD
            pow10[i + 1] = (pow10[i] * 10) % MOD

        ans = []

        for l, r in queries:

            left = bisect_left(pos, l)
            right = bisect_right(pos, r)

            if left == right:
                ans.append(0)
                continue

            # digit sum
            digit_sum = (prefix_sum[right] - prefix_sum[left]) % MOD

            # extract number
            length = right - left

            x = (
                prefix_num[right]
                - (prefix_num[left] * pow10[length])
            ) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans
