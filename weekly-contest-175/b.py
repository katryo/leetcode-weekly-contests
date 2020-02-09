from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)

        ans = 0
        for key, count in s_counter.items():
            t_count = t_counter[key]
            diff = count - t_count
            if diff > 0:
                ans += diff
        return ans