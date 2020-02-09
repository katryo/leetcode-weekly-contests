from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        n = len(seats)
        m = len(seats[0])

        def gen_arrangements(i):
            row = seats[i]
            ret = []

            def helper(cur, j):
                if len(cur) == m:
                    s_count = 0
                    for c in cur:
                        if c == 's':
                            s_count += 1
                    ret.append((s_count, ''.join(cur)))
                    return
                if row[j] == '.':
                    if not cur or (cur and cur[-1] != 's'):
                        cur.append('s')
                        helper(cur, j+1)
                        cur.pop()
                    cur.append('x')
                    helper(cur, j+1)
                    cur.pop()
                else:
                    cur.append('#')
                    helper(cur, j+1)
                    cur.pop()

            helper([], 0)
            return ret

        top_arr = gen_arrangements(0)

        dp = {}
        for arrange in top_arr:
            dp[arrange[1]] = arrange[0]

        def is_possible(lower, upper):
            for i in range(m):
                if lower[i] == 's':
                    if i > 0 and upper[i-1] == 's':
                        return False
                    if i < m-1 and upper[i+1] == 's':
                        return False
                    if i > 0 and lower[i-1] == 's':
                        return False
                    if i < m-1 and lower[i+1] == 's':
                        return False
            return True

        for i in range(1, n):
            arrangements = gen_arrangements(i)

            next_dp = {}
            for arrange in arrangements:
                possible_max = -1
                for key, count in dp.items():
                    if is_possible(arrange[1], key):
                        possible_max = max(possible_max, count)
                if possible_max != -1:
                    next_dp[arrange[1]] = arrange[0] + possible_max
            dp = next_dp

        ans = 0
        for count in dp.values():
            ans = max(ans, count)
        return ans


# s = Solution()
# print(s.maxStudents([[".","#"],
#                      ["#","#"],
#                      ["#","."],
#                      ["#","#"],
#                      [".","#"]]))
# print(s.maxStudents([[".",".","#","#"],
#                      [".","#",".","."],
#                      ["#",".",".","#"],
#                      ["#","#","#","."]]))
# print(s.maxStudents([[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]))
# print(s.maxStudents([["#",".",".",".","#"],
#                 [".","#",".","#","."],
#                 [".",".","#",".","."],
#                 [".","#",".","#","."],
#                 ["#",".",".",".","#"]]))


