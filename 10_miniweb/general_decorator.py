def set_func1(func):
    print("--begin  set_func1")

    def call_func(*args, **kwargs):
        print("--this is enhance1")
        return func(*args, **kwargs)

    return call_func


def set_func2(func):
    print("--begin set_func2")

    def call_func(*args, **kwargs):
        print("--this is enhance2")
        return func(*args, **kwargs)

    return call_func


@set_func1
@set_func2
def test1(num, *args, **kwargs):
    print("---test1")
    return "ok"


test_ = test1(100)
print(test_)
