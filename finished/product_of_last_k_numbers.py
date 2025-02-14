# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.cur_prod = 1
        self.prods = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.cur_prod = 1
            self.prods = [1]
        else:
            self.cur_prod *= num
            self.prods.append(self.cur_prod)
        # print(num, self.cur_prod, self.prods)

    def getProduct(self, k: int) -> int:
        # print(k)
        if k >= len(self.prods):
            return 0
        return self.cur_prod // self.prods[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)