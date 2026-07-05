from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        directions = [(1, 0), (0, 1), (1, 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue

                best = -1
                count = 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy

                    if ni < n and nj < n and score[ni][nj] != -1:
                        if score[ni][nj] > best:
                            best = score[ni][nj]
                            count = ways[ni][nj]
                        elif score[ni][nj] == best:
                            count = (count + ways[ni][nj]) % MOD

                if best == -1:
                    continue

                value = int(board[i][j]) if board[i][j].isdigit() else 0
                score[i][j] = best + value
                ways[i][j] = count

        return [score[0][0], ways[0][0]] if ways[0][0] else [0, 0]
