import matplotlib.pyplot as plt
import random
from matplotlib import font_manager

# 假设大家在30岁的时候,根据自己的实际情况,统计出来了你和你同桌各自从11岁到30岁每年交的女(男)朋友的数量如列表a和b,
# 请在一个图中绘制出该数据的折线图,以便比较自己和同桌20年间的差异,同时分析每年交女(男)朋友的数量走势
y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
x = range(11, 31)
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y1, label='小明', color='r', linestyle='--')
plt.plot(x, y2, label='小红', color='cyan', linestyle=':')
plt.legend(prop=my_font,loc='best')
plt.savefig('./trend.png')
plt.show()
