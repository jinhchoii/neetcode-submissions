class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row, col, visited):
            # Check boundaries
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # Already visited
            if (row, col) in visited:
                return

            visited.add((row, col))

            # Explore four directions
            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # Check boundaries
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue

                # Only move to equal or higher land
                if heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, visited)

        # Start DFS from Pacific and Atlantic edges
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        # Find cells that can reach both oceans
        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result