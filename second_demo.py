# __author__: "yudongyue"
# date: 2021/3/22
import matplotlib.pyplot as plt
import numpy as np

#  一次性添加所有画纸
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0, 0].set(title='Upper Left')
axes[0, 1].set(title='Upper Right')
axes[1, 0].set(title='Lower Left')
axes[1, 1].set(title='Lower Right')
plt.show()
