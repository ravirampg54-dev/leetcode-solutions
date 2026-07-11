from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            vertices = 1
            degree_sum = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    v, d = dfs(nei)
                    vertices += v
                    degree_sum += d

            return vertices, degree_sum

        for i in range(n):
            if not visited[i]:
                vertices, degree_sum = dfs(i)

                if degree_sum == vertices * (vertices - 1):
                    ans += 1

        return ans
