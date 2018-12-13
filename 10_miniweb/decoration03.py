def enhance(func):
    def print_a(*args, **kwargs):
        print("---enhance---")
        func(*args, **kwargs)

    return print_a


@enhance  # 等价于get_aa = enhance(get_aa)
def get_aa(num, *args, **kwargs):
    print('---test1-- %d' % num)
    print('hello_world', args)
    print('hello_world', kwargs)


@enhance
def get_bb(a, b, c):
    print("value %d " % (a + b + c))


get_aa(100, 200, 300, tom=22)
get_bb(1, 2, 3)
