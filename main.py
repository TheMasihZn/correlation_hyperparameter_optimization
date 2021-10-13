
import librosa.display
import numpy as np
from Operations import run_this
import pickle

scale, sr = librosa.load("audio/scale.wav")

results = []
count = 0
for i in range(1, 1000, 1):
    r = []
    for j in range(10, 1000, 1):
        step = i
        v_length = j
        limitD = 1000
        limitU = limitD + j
        q_vector = scale[limitD: limitU]

        f_results, overlap, t = run_this(scale, q_vector, limitD, limitU, step, f"r/{count}.png")
        if overlap > 90:
            r.append([step, v_length, f_results, t, overlap, count])
        count += 1
        print(f"{i}*{j} in {t}")
    results.append(r)

for r in results:
    r.sort(reverse=True, key=lambda o: o[4])
results = np.array(results, dtype=object)

with open("r/results.txt", "wb") as fp:
    pickle.dump(results, fp)




