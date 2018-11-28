def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


gl_nums = (1, 2, 3)
gl_dict = {"name": "eryeer"}
demo(1, 2, 3, 4, 5, name="小明", age=18)
demo(1, *gl_nums, **gl_dict)
