import matplotlib.pyplot as plt
import matplotlib
import random
from matplotlib import font_manager

# 如果列表a表示10点到12点的每一分钟的气温,如何绘制折线图观察每分钟气温的变化情况?
#        a= [random.randint(20,35) for i in range(120)]

# font = {'family': 'monospace',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc("font", **font)

y = [random.randint(20, 35) for i in range(120)]
x = range(120)
plt.figure(figsize=(20, 8), dpi=180)
plt.plot(x, y)
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)
# plt.xticks(_x[::3], _xtick_labels[::3], rotation=90)
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度 单位(℃)', fontproperties=my_font)
plt.title('10点到12点每分钟温度变化', fontproperties=my_font)
plt.grid(alpha=0.2)
plt.savefig('./temper.png')
plt.show()
