class Decorators:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("--enhance ---")
        return self.func(*args, **kwargs)


@Decorators
def test(a):
    print("hello world %s" % a)


test('yes')