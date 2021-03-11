class Solution:
    def minimumTotal(self, triangle: List[List[int]]):
        rows = len(triangle)
        cols = len(triangle[-1])
        if len(triangle) == 1:
            return triangle[0][0]
        min_arr = triangle[:]
        for i in range(len(triangle) - 1, 0, -1):
            for j in range(len(triangle[i-1])):
                cur = triangle[i-1][j]
                min_arr[i-1][j] = min(cur + triangle[i][j],
                                      cur + triangle[i][j+1])
        return min(min_arr[0])
