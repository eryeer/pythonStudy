class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s jump and play" % self.name)


class XiaoDog(Dog):

    def game(self):
        print("%s fly to sky" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s and %s play" % (self.name, dog.name))
        dog.game()


wangcai = Dog("wangcai")
xiaoming = Person("xiaoming")
xiaodog = XiaoDog("xiaotian")
xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(xiaodog)
