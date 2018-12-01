from collections.abc import Iterable
from collections.abc import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("老王")
classmate.add("老張")
classmate.add("老三")

print("if is iterable:", isinstance(classmate, Iterable))
classmate_iterator = iter(classmate)
print("classmate_iterator is iterator:", isinstance(classmate, Iterator))
for name in classmate:
    print(name)
