from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        minutes = 0

        # Step 1: Find all rotten oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))

        # Step 2: BFS
        while queue:
            size = len(queue)
            changed = False

            for i in range(size):
                row, col = queue.popleft()

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

                    # Check whether the adjacent orange is fresh
                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                        changed = True

            # One minute passes if oranges became rotten
            if changed:
                minutes += 1

        # Step 3: Check for remaining fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return minutes