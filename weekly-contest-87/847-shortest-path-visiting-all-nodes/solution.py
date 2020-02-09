import heapq

class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        explored = set()
        q = [(0, 0)]

        consumed = 0

        while len(explored) != len(graph):
            node = heapq.heappop(q)
            consumed = node[1]
            explored.add(node[0])
            for n in node:
                heapq.heappush(q, (1+node[1], n))
        return consumed

s = Solution()
print(s.shortestPathLength([[1,2,3],[0],[0],[0]]))
print(s.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))
