class ProductOfNumbers:

    def __init__(self):
        self.prod_so_far = []
        self.zero_count = []
        self.arr = []

    def add(self, num: int) -> None:
        self.arr.append(num)
        if self.prod_so_far:
            last = self.prod_so_far[-1]
            if last == 0:
                self.prod_so_far.append(num)
            else:
                self.prod_so_far.append(last * num)
        else:
            self.prod_so_far.append(num)

        if self.zero_count:
            if num == 0:
                self.zero_count.append(self.zero_count[-1] + 1)
            else:
                self.zero_count.append(self.zero_count[-1])
        else:
            if num == 0:
                self.zero_count.append(1)
            else:
                self.zero_count.append(0)

    def getProduct(self, k: int) -> int:
        last = self.prod_so_far[-1]

        if len(self.prod_so_far) == k:
            if self.zero_count[-1] == 0:
                return last
            else:
                return 0
        accum = self.prod_so_far[-1 - k]

        # print('k', k, self.prod_so_far)
        # print('zero_count', self.zero_count)
        if self.zero_count[-k - 1] != self.zero_count[-1]:
            return 0
        if accum == 0:
            return last
        return last // accum

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)