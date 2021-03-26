# __author__: "yudongyue"
# date: 2021/3/25
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.gridspec import GridSpec
import os
import shutil
import time

fig = plt.figure(figsize=(15, 5))
# ax_1 = fig.add_subplot(1, 3, 1)
# ax_2 = fig.add_subplot(132)
# ax_3 = fig.add_subplot(133)
# plt.tight_layout(0)
gs = GridSpec(1, 3, figure=fig)  # GridSpec将fiure分为1行3列，每行三个axes，gs为一个matplotlib.gridspec.GridSpec对象，可灵活的切片figure
for one_key in range(3):
    # color_list = ['#5A6CA6', '#E9BCC7', '#D98433']
    color_list = ['navy', '#E9BCC7', '#D98433']
    x_list = [0.38, 0.295, 0.35]
    ax = fig.add_subplot(gs[0, one_key])
    plt.tight_layout(0)
    circle = Circle(xy=(0.5, 0.4), radius=0.4, color=color_list[one_key], alpha=1)
    ax.add_patch(circle)
    # ax.plot([0.5, 0.5, 0.5], [0.8, 0.81, 0.82], color='red', marker='+')
    ax.axis('off')
    Ele_data = [['总用电量(KWh)', '日平均用电量（KWh）', '总电费（RMB）'], [8611248, 277782, 5925686]]
    ax.text(x_list[one_key], 0.9, Ele_data[0][one_key], fontsize=30, color='black')
    ax.text(0.3, 0.4, str(Ele_data[1][one_key]), fontsize=40, color='r')
plt.show()
path = './/plot_folder_user//'
if os.path.isdir(path):
    shutil.rmtree(path)
    time.sleep(2)
    os.makedirs(path)
else:
    os.makedirs(path)
plt.savefig(path + '总用电量统计.jpg')
plt.cla()
plt.close("all")
