class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(i, j, iw) -> bool:
            if iw == len(word):
                return True

            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[iw]:
                return False

            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, iw + 1) or dfs(i - 1, j, iw + 1) or dfs(i, j + 1, iw + 1) or dfs(i, j - 1, iw + 1)
            board[i][j] = tmp

            return res

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
