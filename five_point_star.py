# __author__: "yudongyue"
# date: 2021/4/6


import numpy as np

import matplotlib.pyplot as plt

# # barSlices = 5
# fig = plt.figure(figsize=(10, 6))
# ax = fig.add_subplot(111, polar=True)
# theta = np.linspace(0.0, 2 * np.pi, 5, endpoint=False)  # 角度
# # r = 30 * np.random.rand(barSlices)  # 值
# r = [30, 30, 30, 30, 30]
# plt.polar(theta, r, color="chartreuse", linewidth=5, marker="*", mfc="b", ms=6)
# # angles = np.linspace(0, 2 * np.pi, 5, endpoint=False)
# # for i in range(5):
# #     ax.plot([angles[i], angles[i]], [0, 30], '--', lw=0.5, color='blue')
# # # mfc-------->星的颜色  ms-------->星的大小
# # for i in range(5):
# #     ax.plot([angles[i], angles[i]], [0, 30], '--', lw=0.5, color='blue')
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

'''
    极坐标分为：极径和角度

'''
r = [5, 5, 5, 5, 5, 5]
theta = [i * np.pi / 2 for i in range(5)]
theta = [0, 2 * np.pi / 5, 4 * np.pi / 5, 6 * np.pi / 5, 8 * np.pi / 5, 0]
print(theta)
ax = plt.subplot(111, projection='polar')
# projection = 'polar' 指定为极坐标

ax.plot(theta, r, linewidth=3, color='red')
# 第一个参数为角度，第二个参数为极径

ax.grid(True)  # 是否有网格

plt.show()
