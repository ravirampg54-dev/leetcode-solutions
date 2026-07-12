from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}

        # Assign rank to each unique value
        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i

        # Replace each element with its rank
        return [rank[num] for num in arr]
