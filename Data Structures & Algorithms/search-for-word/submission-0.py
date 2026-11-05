class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):

            # Found every letter
            if index == len(word):
                return True

            # Check boundaries
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            # Check if the letter matches
            if board[row][col] != word[index]:
                return False

            # Mark the cell as visited
            temp = board[row][col]
            board[row][col] = "#"

            # Explore all four directions
            found = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
            )

            # Backtrack: restore the original letter
            board[row][col] = temp

            return found

        # Find a starting cell matching the first letter
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return False