# __author__: "yudongyue"
# date: 2021/3/22
#  plot画出一系列点，然后用线连起来
import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()
x = np.linspace(0, np.pi)
y_sin = np.sin(x)
y_cos = np.cos(x)
ax1 = figure.add_subplot(221)
ax2 = figure.add_subplot(222)
ax3 = figure.add_subplot(223)
ax1.plot(x, y_sin)
ax2.plot(x, y_sin, 'go--', linewidth=2, markersize=12)
ax3.plot(x, y_cos, color='red', marker='+', linestyle='dashed')
plt.show()
