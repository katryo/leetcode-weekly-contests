class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        ans = 0
        for row in grid:
            for i in range(n):
                # i == 1 => n-1 nega num
                if row[i] < 0:
                    # i is the first negative number in the row
                    ans += (n - i)
                    break
        return ans