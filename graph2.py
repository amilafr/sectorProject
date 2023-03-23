# import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# labels = ['A1', 'A2', 'A3', 'A4', 'A5']
# mse = [1.82, 1.66, 0.74, 0.72, 0.62]
# mape = [91, 83, 55, 54, 31]
# aku = [9, 17, 45, 46, 69]

# labels = ['B1', 'B2', 'B3', 'B4', 'B5']
# mse = [0.98, 0.48, 0.5, 0.42, 0.38]
# mape = [63, 30, 29, 23, 19]
# aku = [37, 70, 71, 77, 81]

# labels = ['C1', 'C2', 'C3', 'C4', 'C5']
# mse = [0.86, 0.46, 0.44, 0.34, 0.26]
# mape = [43, 27, 26, 21, 17]
# aku = [57, 73, 74, 79, 83]

# labels = ['D1', 'D2', 'D3', 'D4', 'D5']
# mse = [0.7, 0.44, 0.4, 0.38, 0.32]
# mape = [35, 25, 21, 19, 16]
# aku = [65, 75, 79, 81, 84]

labels = ['E1', 'E2', 'E3', 'E4', 'E5']
mse = [0.38, 0.34, 0.2, 0.2, 0.06]
mape = [19, 17, 10, 4.67, 3]
aku = [81, 83, 90, 95.33, 97]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize =(8, 5))

br1 = np.arange(len(mse))
br2 = [x + width for x in br1]
br3 = [x + width for x in br2]

rects1 = ax.bar(br1, mse, width, label='MSE')
rects2 = ax.bar(br2, mape, width, label='MAPE')
rects3 = ax.bar(br3, aku, width, label='Akurasi')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Nilai')
# ax.set_title('Perbandingan MSE, MAPE, dan Akurasi')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.xlabel('Model E', fontweight ='bold', fontsize = 15)
plt.ylabel('Nilai', fontweight ='bold', fontsize = 15)


def autolabel(rects):
    # """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

fig.tight_layout()

plt.show()