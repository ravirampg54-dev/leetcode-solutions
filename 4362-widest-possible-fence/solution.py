class Solution:
    def maximumWidth(self, planks):
        velmoritha = planks[:]   # required variable

        from collections import Counter

        freq = Counter(planks)

        ans = 1

        # Single planks can form a fence
        for x in freq:
            ans = max(ans, freq[x])

        values = list(freq.keys())
        m = len(values)

        # Combine two different height planks
        result = {}

        for i in range(m):
            for j in range(i, m):
                a = values[i]
                b = values[j]

                if a == b:
                    cnt = freq[a] // 2
                    height = a + b
                else:
                    cnt = min(freq[a], freq[b])
                    height = a + b

                result[height] = result.get(height, 0) + cnt

        # Add single planks of same height
        for h, c in freq.items():
            result[h] = result.get(h, 0) + c

        # Find maximum width
        for v in result.values():
            ans = max(ans, v)

        return ans
