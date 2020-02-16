from typing import List
from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)

        max_end = float('-inf')
        dic = defaultdict(list)
        for i in range(n):
            start, end = events[i]
            max_end = max(max_end, end)
            dic[start].append(end)

        heap = []

        ans = 0
        for i in range(1, max_end+1):
            if i in dic:
                for end in dic[i]:
                    heappush(heap, end)

            while heap:
                end_to_go = heappop(heap)
                if end_to_go < i:
                    continue
                ans += 1
                break

        return ans


# s = Solution()
# print(s.maxEvents([[1,2],[2,3],[3,4]]))
# print(s.maxEvents([[1,2],[2,3],[3,4],[1,2]]))
# print(s.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))
# print(s.maxEvents([[1,100000]]))
# print(s.maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]]))
# print(s.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]]))
# print(s.maxEvents([[1,10],[2,2],[2,2],[2,2],[2,2]]))
# print(s.maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]))
