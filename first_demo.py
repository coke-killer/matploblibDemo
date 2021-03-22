# __author__: "yudongyue"
# date: 2021/3/22
import matplotlib.pyplot as plt

#   首先获取figure对象
fig = plt.figure()
#  添加可以真正作画的纸
ax = fig.add_subplot(223)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An example Axes', ylabel='Y-Axis', xlabel='X-Axis')
plt.show()
