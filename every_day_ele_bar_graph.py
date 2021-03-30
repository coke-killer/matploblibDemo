# __author__: "yudongyue"
# date: 2021/3/26
import matplotlib.pyplot as plt
import pandas as pd

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
ax.bar(xlist, day_ele_all['总用电量'], color='orange')
# plt.grid(axis='y')
plt.xticks(rotation=-30)  # 斜着展示，角度从逆时针开始算。
plt.title('每日用电量统计', fontsize=25, ha="center")
plt.xlabel('时间（日）')
plt.ylabel('用电量（KWh）')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
path = './/plot_folder_user//'
plt.savefig(path + '每日用电量统计')
plt.cla()
plt.close("all")
