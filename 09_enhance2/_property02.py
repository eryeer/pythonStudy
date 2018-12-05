class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

    MONEY = property(setMoney, getMoney)


money = Money()
money.money = 1000
print(money.money)
# del money.money
# print(money.money)
