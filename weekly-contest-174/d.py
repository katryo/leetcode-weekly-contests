from typing import List
from collections import defaultdict


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        graph = defaultdict(list)
        for i in range(n):
            hi = arr[i]
            # left
            for j in range(i-1, max(-1, i-d-1), -1):
                if arr[j] >= hi:
                    break
                graph[i].append(j)

            for j in range(i+1, min(n, i+d+1)): # test
                if arr[j] >= hi:
                    break
                graph[i].append(j)

        dp = [0] * n

        def helper(i):
            if dp[i]:
                return dp[i]
            if i not in graph:
                return 1
            cand = 0
            for child in graph[i]:
                cand = max(cand, helper(child))
            cand += 1
            dp[i] = cand
            return cand

        for j in range(n):
            helper(j)

        ans = max(dp)
        if ans == 0:
            return 1
        return ans


# s = Solution()
# print(s.maxJumps([40,98,14,22,45,71,20,19,26,9,29,64,76,66,32,79,14,83,62,39,69,25,92,79,70,34,22,19,41,26,5,82,38], 6))
# print(s.maxJumps([7,6,5,4,3,2,1], 1))
# print(s.maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2))
# print(s.maxJumps([3,3,3,3], 3))
# print(s.maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2))
