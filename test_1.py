# __author__: "yudongyue"
# date: 2021/3/22
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(x, y)
ax2.plot(x, y)
ax2.set_xlim([-1, 6])
ax2.set_ylim([-1, 3])
plt.show()
