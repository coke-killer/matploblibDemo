# __author__: "yudongyue"
# date: 2021/3/22
import matplotlib.pyplot as plt
import numpy as np

data = np.shape(2, )
data2 = np.shape(2, 3)
fig, (ax1, ax2) = plt.subplots(2)
ax1.boxplot(data)
ax2.boxplot(data2, vert=False)
plt.show()
