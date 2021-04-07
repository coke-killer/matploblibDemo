# __author__: "yudongyue"
# date: 2021/4/6
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pylab import mpl

# mpl.rcParams['font.sans-serif'] = ['SimHei']
# mpl.rcParams['axes.unicode_minus'] = False

labels = [u'娱乐', u'汽车', u'房屋', u'食物']
colors = ['silver', 'orange', 'dimgrey', 'tan']
sizes = [5, 20, 41, 34]
explode = [0.1, 0.1, 0.1, 0.1]
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.0f%%', shadow=False, pctdistance=0.5,
       startangle=0, textprops={'fontsize': 15, 'color': 'w'})
ax.axis('equal')
font_microsoft = FontProperties(fname=r"C:\Windows\Fonts\msyhbd.ttc", size="17")
plt.title("实际支出摘要", color='k', fontproperties=font_microsoft)
ax.legend(bbox_to_anchor=(0.75, -0.05), frameon=False, ncol=4, fontsize=15, handletextpad=0.5)
plt.show()
