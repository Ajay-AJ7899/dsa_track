
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        rows = len(graph)
        color = [-1] * rows

        def dfs(node):
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]

                    if not dfs(neighbor):
                        return False

                elif color[neighbor] == color[node]:
                    return False

            return True

        for i in range(rows):
            if color[i] == -1:
                color[i] = 0

                if not dfs(i):
                    return False

        return True
