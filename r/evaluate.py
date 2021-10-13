import numpy as np
import pickle
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.pyplot import figure
from scipy.special import expit as sigmoid

with open("results.txt", "rb") as fp:
    b = pickle.load(fp)

b = np.array(b)

# sample
minn = [1, 11, (1.0, 1000), 100, 100.00000000000001, 1]
for row in b:
    if len(row) > 0:
        for col in row:
            if col[3] <= minn[3]:
                minn = col
minn = []
for row in b:
    if len(row) > 0:
        for col in row:
            minn.append(col)

minn.sort(reverse=False, key=lambda _t: _t[3])

print(f"steps = {minn[0][0]}, \nvector length = {minn[0][1]}, \nin {minn[2][3]}")
print(f"steps = {minn[1][0]}, \nvector length = {minn[2][1]}, \nin {minn[3][3]}\n")
print(f"steps = {minn[2][0]}, \nvector length = {minn[3][1]}, \nin {minn[4][3]}\n")
print(f"steps = {minn[3][0]}, \nvector length = {minn[4][1]}, \nin {minn[1][3]}\n")
print(f"steps = {minn[4][0]}, \nvector length = {minn[1][1]}, \nin {minn[1][3]}\n")
ts = []
steps = []
v_lengths = []
for row in [cole for i, cole in enumerate(b) if i % 100 is 0]:
    if len(row) > 0:
        if len(row[0]) > 0:
            ts.append(sigmoid(row[0][3]))
            steps.append(row[0][0])
            v_lengths.append(row[0][1])
b = np.array(b)
#
maxts = max(ts)
mints = min(ts)
for i, t in enumerate(ts):
    ts[i] = t



fig, ax = plt.subplots()
ax.set_xticks(steps)
ax.set_yticks(v_lengths)
plt.hist2d(steps, v_lengths, len(steps), weights=ts)
cb = plt.colorbar()
cb.set_label("counts in bins")
plt.show()
#