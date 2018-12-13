def enhance(func):
    def print_a():
        print("---enhance---")
        func()

    return print_a


@enhance  # 等价于get_aa = enhance(get_aa)
def get_aa():
    print('hello_world')


get_aa()
