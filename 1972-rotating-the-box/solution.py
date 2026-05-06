class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Step 1: Simulate gravity on each row
        for row in boxGrid:
            empty = n - 1

            for col in range(n - 1, -1, -1):

                # Obstacle resets position
                if row[col] == '*':
                    empty = col - 1

                # Move stone to the rightmost empty place
                elif row[col] == '#':
                    row[col], row[empty] = '.', '#'
                    empty -= 1

        # Step 2: Rotate 90 degrees clockwise
        result = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = boxGrid[i][j]

        return result
