class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):
            # Check boundaries
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # Stop if the cell is not "O"
            if board[row][col] != "O":
                return

            # Mark this cell as safe
            board[row][col] = "S"

            # Explore all four directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Step 1: Start DFS from border cells
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)

            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)

        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)

            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        # Step 2: Capture surrounded regions
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"

                elif board[row][col] == "S":
                    board[row][col] = "O"