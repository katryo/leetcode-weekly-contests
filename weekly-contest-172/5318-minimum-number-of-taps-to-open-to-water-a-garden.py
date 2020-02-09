from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        lr = []
        for i in range(n+1):
            if ranges[i] == 0:
                continue
            l = max(0, i - ranges[i])
            r = i + ranges[i]
            lr.append((l, r))

        lr.sort()

        lenlr = len(lr)

        cover = -1
        cur = 0
        ans = 0
        for i in range(n+1):
            if i == n and i == cover:
                continue
            if i < cover:
                continue
            rightmost = -1
            while cur < lenlr and lr[cur][0] <= i:
                rightmost = max(rightmost, lr[cur][1])
                cur += 1
            if rightmost == -1:
                return -1
            ans += 1
            cover = rightmost
        return ans


# s = Solution()
# print(s.minTaps(35, [1,0,4,0,4,1,4,3,1,1,1,2,1,4,0,3,0,3,0,3,0,5,3,0,0,1,2,1,2,4,3,0,1,0,5,2]))
# print(s.minTaps(5, [3,4,1,1,0,0]))
# print(s.minTaps(3, [0,0,0,0]))
# print(s.minTaps(7,  [1,2,1,0,2,1,0,1]))
# print(s.minTaps( 8,  [4,0,0,0,0,0,0,0,4]))
# print(s.minTaps(8,  [4,0,0,0,4,0,0,0,4]))
