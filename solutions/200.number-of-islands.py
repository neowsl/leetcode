class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])

        visited = [[False for _ in range(N)] for _ in range(M)]

        res = 0

        def dfs(i: int, j: int):
            if i < 0 or i >= M or j < 0 or j >= N or visited[i][j] or grid[i][j] == "0":
                return

            visited[i][j] = True
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(M):
            for j in range(N):
                if grid[i][j] == "0" or visited[i][j]:
                    continue

                res += 1
                dfs(i, j)

        return res
