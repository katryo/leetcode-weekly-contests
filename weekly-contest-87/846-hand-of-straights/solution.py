import collections

class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W != 0:
            return False

        hand.sort()
        d = collections.OrderedDict()
        for card in hand:
            if card in d:
                d[card] += 1
            else:
                d[card] = 1

        hands_to_be_made = len(hand) // W

        for _ in range(hands_to_be_made):
            if not d.keys:
                return False
            smallest = list(d)[0]
            for i in range(smallest, smallest+W):
                if i not in d:
                    return False
                if d[i] == 1:
                    del d[i]
                else:
                    d[i] -= 1
        return True

s = Solution()
print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(s.isNStraightHand([1,2,3,4,5], 4))
