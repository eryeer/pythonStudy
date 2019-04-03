import matplotlib.pyplot as plt

# 设置图片大小，清晰度
#plt.figure(figsize=(20, 20), dpi=180)
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
plt.plot(x, y)
plt.xticks(x[::2])
plt.savefig('./test.png')

# plt.show()
