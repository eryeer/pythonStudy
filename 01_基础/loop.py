import print2


def loop_while():
    """

    :return: result sum of compute
    """
    result = 0
    # 1. 计数器
    i = 0
    # 2. 开始循环
    while i <= 100:
        # 判断偶数
        if i % 2 == 0:
            print(i)
            result += i
        # 处理计数器
        i += 1
    print("0~100之间偶数求和结果 = %d" % result)
    return result


loop_while()
print2.print1()
