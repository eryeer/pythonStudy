# #!/usr/bin/python
# # coding:utf-8
# # import matplotlib.pyplot as plt
# # import numpy as np
# # import pandas as pd
#
# # fig, ax = plt.subplots()
# #
# # plt.subplot(4, 1, 4)
# # data = pd.DataFrame(np.random.randn(1000, 4), columns=['x', 'y', 'z', 't'])
# # index = range(len(data))
# #
# # plt.plot(index, data['x'].cumsum(), label='xxx')
# #
# # plt.subplot(4, 1, 2)
# # plt.plot(index, data.loc[:, ['x', 'y']].cumsum())
# #
# #
# # plt.subplot(4, 1, 3)
# # plt.plot(index, data.loc[:, ['x', 'y', 'z']].cumsum())
# #
# # plt.subplot(4, 1, 4)
# # plt.plot(index, data.cumsum())
# #
# # fig.set_size_inches(40, 32)
# # plt.show()
#
# class A:
#     def __init__(self):
#         self.n = 2
#
#     def add(self, m):
#         print('self is {0} @A.add'.format(self))
#         self.n += m
#
#
# class B(A):
#     def __init__(self):
#         self.n = 3
#
#     def add(self, m):
#         print('self is {0} @B.add'.format(self))
#         super().add(m)
#         self.n += 3
#
# class C(A):
#     def __init__(self):
#         self.n = 4
#
#     def add(self, m):
#         print('self is {0} @C.add'.format(self))
#         super().add(m)
#         self.n += 4
#
#
# class D(B, C):
#     def __init__(self):
#         self.n = 5
#
#     def add(self, m):
#         print('self is {0} @D.add'.format(self))
#         super().add(m)
#         self.n += 5
#
# if __name__ == "__main__":
#     d = D()
#     d.add(2)
#     print(d.n)

import os
for folderName, subfolders, filenames in os.walk('pandas'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')