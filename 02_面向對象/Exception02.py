try:
    num = int(input("pls input a num"))
    result = 8 / num
except ValueError:
    print("输入参数错误")
# except ZeroDivisionError:
#     print("除零错误")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("attempt success")
finally:
    print("execute whatever fail or success")

print("------" * 2)
