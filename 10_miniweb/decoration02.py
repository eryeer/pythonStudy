def enhance(func):
    def print_a(num):
        print("---enhance---")
        func(num)

    return print_a


@enhance  # 等价于get_aa = enhance(get_aa)
def get_aa(num):
    print('hello_world %d' % num)


get_aa(10)
