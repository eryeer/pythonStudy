import copy

a = [11, 22]
b = a
print(id(a))
print(id(b))

c = copy.deepcopy(a)
print(id(c))

# 如果用copy.copy 、copy.deepcopy对一个全部都是不可变类型的数据进行拷贝，那么他们结果相同，都是引用指向
# 如果拷贝的是一个拥有不可变类型的数据，计是元祖是最顶层，那么deepcopy依然是深拷贝，而copy.copy还是指向
# 列表切片是浅拷贝
# 字典里的拷贝也是浅拷贝，字典里value存储的是一个指针，拷贝后指针也被拷贝，指向相同value地址

