class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def dfs(row, col):

            # Outside the grid
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # Water or already visited
            if grid[row][col] != "1":
                return

            # Mark land as visited
            grid[row][col] = "0"

            # Explore all four directions
            dfs(row + 1, col)  # Down
            dfs(row - 1, col)  # Up
            dfs(row, col + 1)  # Right
            dfs(row, col - 1)  # Left

        # Check every cell
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands