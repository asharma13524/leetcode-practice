class Solution:
    def uniquePaths(self, m: int, n: int):
        # Build up array from same row, prev col, and same col, prev row
        if not m or not n:
            return 0
        arr = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i][j-1] + arr[i-1][j]
        return arr[-1][-1]

        # save space O(n) here by only storing col
        if not m or not n:
            return 0
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
