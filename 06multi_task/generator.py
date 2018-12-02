def create_num(all_num):
    print("---1---")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("---2---")
        # print(a)
        yield a  # 如果一個函數中有yield語句，那麽這個就不再是函數，而是一個生成器模板
        print("---3---")
        a, b = b, a + b
        current_num += 1
        print("---4---")
    return "----ok-----"

# 如果再調用create_num的時候，發現這個函數中有yield，那麽此時，不是調用函數，而是創建一個生成器對象
obj = create_num(2)

# for num in obj:
#     print(num)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break
