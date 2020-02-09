class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(A) < 3:
            return 0

        end = 1
        # while end != len(A) and A[end] <= A[end-1]:
        #     end += 1
        #
        # if end == len(A):
        #     return 0
        # assert A[end] > A[end-1]

        ans = 0
        while end < len(A):
            while end != len(A) and A[end] <= A[end-1]:
                end += 1
            start = end-1
            up = False
            down = False

            while end != len(A) and A[end] > A[end-1]:
                if not up:
                    up = True
                end += 1
            assert end == len(A) or A[end] <= A[end-1]

            while end != len(A) and A[end] < A[end-1]:
                if not down:
                    down = True
                end += 1
            assert end == len(A) or A[end] >= A[end-1]

            if up and down:
                ans = max(ans, end - start)
        return ans

s = Solution()
print(s.longestMountain([875,884,239,731,723,685]))
print(s.longestMountain([2,1,4,7,3,2,5]))
print(s.longestMountain([2,2,2]))
print(s.longestMountain([2,3,2]))
print(s.longestMountain([2,3,4]))
print(s.longestMountain([0,2,2]))
print(s.longestMountain([5,2,2]))
print(s.longestMountain([5,2,3]))
print(s.longestMountain([5,2,3,1]))
print(s.longestMountain([2,3,3,2,0,2]))
