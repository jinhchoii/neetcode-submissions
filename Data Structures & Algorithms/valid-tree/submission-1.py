class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Step 1: Create adjacency list
        adj = {}

        for node in range(n):
            adj[node] = []

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # Step 2: Create visited set
        visited = set()

        # Step 3: DFS
        def dfs(node, parent):

            # Already visited means cycle
            if node in visited:
                return False

            visited.add(node)
    
            # Explore neighbors
            for neighbor in adj[node]:

                # Don't go back to the parent
                if neighbor == parent:
                    continue

                # Check the neighbor
                if dfs(neighbor, node) == False:
                    return False

            return True

        # Step 4: Start DFS from Node 0
        if dfs(0, -1) == False:
            return False

        # Step 5: Check if all nodes were visited
        if len(visited) != n:
            return False

        return True