class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        parent = []

        for i in range(n + 1):
            parent.append(i)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            parent[root_b] = root_a
            return True

        for a, b in edges:
            if union(a, b) == False:
                return [a, b]

        return []