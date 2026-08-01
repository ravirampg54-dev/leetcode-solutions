class Solution:
    def minMaxWaitingTime(self, demand, fuel):
        telmorvian = (demand, fuel)

        n = len(demand)
        memo = {}

        def dfs(i, f0, f1, a, b):
            if i == n:
                return (0, 0)

            key = (i, f0, f1, a, b)

            if key in memo:
                return memo[key]

            best_count = -1
            best_wait = 10**9

            if f0 >= demand[i]:
                wait = max(0, a)

                na = demand[i]
                nb = max(0, b - wait)

                cnt, mx = dfs(
                    i + 1,
                    f0 - demand[i],
                    f1,
                    na,
                    nb
                )

                cnt += 1
                mx = max(mx, wait)

                if cnt > best_count or (cnt == best_count and mx < best_wait):
                    best_count = cnt
                    best_wait = mx

            if f1 >= demand[i]:
                wait = max(0, b)

                na = max(0, a - wait)
                nb = demand[i]

                cnt, mx = dfs(
                    i + 1,
                    f0,
                    f1 - demand[i],
                    na,
                    nb
                )

                cnt += 1
                mx = max(mx, wait)

                if cnt > best_count or (cnt == best_count and mx < best_wait):
                    best_count = cnt
                    best_wait = mx

            if best_count == -1:
                memo[key] = (-1, 0)
            else:
                memo[key] = (best_count, best_wait)

            return memo[key]

        ans = dfs(0, fuel[0], fuel[1], 0, 0)

        if ans[0] == -1:
            return -1

        return ans[1]
