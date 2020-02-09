import collections


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sd = collections.deque()
        td = collections.deque()

        for s in S:
            if s == '#':
                if sd:
                    sd.pop()
            else:
                sd.append(s)

        for s in T:
            if s == '#':
                if td:
                    td.pop()
            else:
                td.append(s)
        return sd == td


s = Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
print(s.backspaceCompare("ab##", "c#d#"))
print(s.backspaceCompare("a##c", "#a#c"))
print(s.backspaceCompare("a#c",  "b"))
