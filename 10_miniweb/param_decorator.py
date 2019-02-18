def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("---权限验证1---")
            elif level_num == 2:
                print("---权限验证2---")
            return func()
        return call_func
    return set_func


"""
1.调用set_func 并且将1当作实参传递
2.用上一步调用的返回值 当作装饰器对test1函数进行装饰
"""


@set_level(1)
def test1():
    print("--test1--")
    return "ok"


@set_level(2)
def test2():
    print("--test2--")
    return "ok"


test1()
test2()
