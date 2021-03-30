# __author__: "yudongyue"
# date: 2021/3/26
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties

day_ele_all_a = {
    "总用电量": [
        284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900,
        284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900,
        284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900,
        284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900, 284721.335900,
        284721.335900, 284721.335900, 284721.335900
    ]}
day_ele_all = pd.DataFrame(day_ele_all_a)
day_ele_all.index = day_ele_all.index + 1
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
xlist = [str(i) for i in day_ele_all.index]

plt.xticks(rotation=-30)  # 斜着展示，角度从逆时针开始算。
font_microsoft = FontProperties(fname=r"C:\Windows\Fonts\msyhbd.ttc", size="17")
plt.title('每日用电量统计', fontsize=25, ha="center", fontproperties=font_microsoft)
plt.xlabel('时间（日）', size="15")
plt.ylabel('用电量（KWh）', size="15")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.bar(xlist, day_ele_all['总用电量'], color='orange')
#  设置是否显示刻度
ax.tick_params(bottom=False, left=False, labelsize="15.0")
#   添加辅助线及颜色
plt.grid(axis='y', color="white")
# 设置是否显示边框及颜色
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_color("lightgray")
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color("lightgray")
plt.show()
path = './/plot_folder_user//'
plt.savefig(path + '每日用电量统计')
plt.cla()
plt.close("all")
