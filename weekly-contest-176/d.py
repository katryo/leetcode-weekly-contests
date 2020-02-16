class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)

        while True:
            max_i = -1
            max_v = float('-inf')
            total = 0
            for i in range(n):
                num = target[i]
                total += num
                if num > max_v:
                    max_v = num
                    max_i = i
            diff = total - max_v
            target[max_i] -= diff

            all_one = True
            for i in range(n):
                if target[i] != 1:
                    all_one = False
                if target[i] < 1:
                    return False
            if all_one:
                return True