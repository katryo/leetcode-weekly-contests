from collections import Counter
from typing import List
import math


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        size = len(arr)
        count_num = []
        for num, occur in counter.items():
            count_num.append((occur, num))

        count_num.sort(reverse=True)
        cur = 0
        ans = 0
        for i in range(len(count_num)):
            cur += count_num[i][0]
            ans += 1
            if cur >= math.ceil(size / 2):
                return ans
        assert False


# s = Solution()
# print(s.minSetSize([3,3,3,3,5,5,5,2,2,7]))
# print(s.minSetSize([7,7,7,7,7,7]))
# print(s.minSetSize([1, 9]))
# print(s.minSetSize([1000, 1000, 3, 7]))
# print(s.minSetSize([1,2,3,4,5,6,7,8,9,10]))
