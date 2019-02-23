def upper_attr(class_name, class_parents, class_attr):
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
f = Foo()
print(f.BAR)
