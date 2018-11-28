class A:
    def __init__(self):
        self.num1 = 1000
        self.__num2 = 2000

    def __test(self):
        print("私有方法 %d %d " % (self.num1, self.__num2))


class B(A):
    def demo(self):
        # print("訪問弗雷德私有屬性 %d" % super().__num2)
       print(self.num1) 



b = B()
print(b)

