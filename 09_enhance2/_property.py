class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

    @money.deleter
    def money(self):
        del self.__money


money = Money()
money.money = 1000
print(money.money)
del money.money
print(money.money)
