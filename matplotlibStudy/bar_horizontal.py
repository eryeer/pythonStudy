from matplotlib import pyplot as plt
from matplotlib import font_manager

# 假设你获取到了2017年内地电影票房前20的电影(列表a)和电影票房数据(列表b),那么如何更加直观的展示该数据?
#
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归", "生化危机6：终章",
     "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
plt.figure(figsize=(20, 8), dpi=80)
plt.barh(range(len(a)), b, height=0.3)
plt.yticks(range(len(a)), a, fontproperties=my_font)
plt.savefig('barH.png')
plt.show()