from matplotlib import pyplot as plt
from matplotlib import font_manager

# 假设通过爬虫你获取到了北京2016年3,10月份每天白天的最高气温(分别位于列表a,b),
# 那么此时如何寻找出气温和随时间(天)变化的某种规律?

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12, 13, 6]
x_3 = range(1, 32)
x_10 = range(51, 82)
y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(x_3, y_3, label='3月')
plt.scatter(x_10, y_10, label='10月')

_x = list(x_3) + list(x_10)
_x_desc = ['3月{}日'.format(i) for i in range(1, 32)]
_x_desc += ['3月{}日'.format(i) for i in range(1, 32)]
plt.xticks(_x[::3], _x_desc[::3], rotation=45, fontproperties=my_font)
plt.legend(prop=my_font,loc='upper left')
plt.xlabel("月份",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("温度月份图",fontproperties=my_font)
plt.savefig('./sandian.png')
plt.show()
