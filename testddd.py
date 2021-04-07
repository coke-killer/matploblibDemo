# __author__: "yudongyue"
# date: 2021/4/3
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16.5, 5))
ax = fig.add_subplot()
ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=1, rowspan=1)
ax2 = plt.subplot2grid((1, 3), (0, 1), colspan=2, rowspan=1)
plt.show()
