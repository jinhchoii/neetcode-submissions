class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {}

        for node in range(n):
            adj[node] = []

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count