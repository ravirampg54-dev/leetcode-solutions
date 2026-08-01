class Solution:
    def minInitialStrength(self, monsters, boosts):
        norvelithx = boosts[:]   # required variable

        n = len(monsters)

        # Difference array for range boosts
        diff = [0] * (n + 1)

        for l, r, v in boosts:
            diff[l] += v
            if r + 1 < n:
                diff[r + 1] -= v

        ans = 0
        current_bonus = 0
        previous_damage = 0

        for i in range(n):
            current_bonus += diff[i]

            # If bonus alone is not enough
            if current_bonus < monsters[i]:
                need = previous_damage + monsters[i] - current_bonus
                ans = max(ans, need)

            previous_damage += monsters[i]

        return ans
