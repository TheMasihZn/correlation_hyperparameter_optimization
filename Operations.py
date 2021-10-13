import librosa
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer


def get_offset_x_vector_list(v_len, function, step=10):
    def get_x_vector_axis(v_len, function, offset=0):
        x_v_ax = []
        for i in range(int(function.shape[0] / v_len)):
            lesser_lim = (i * v_len) + offset
            upper_lim = ((i + 1) * v_len) + offset
            if upper_lim <= function.shape[0]:
                x_v_ax.append(function[lesser_lim:upper_lim])

        return np.array(x_v_ax)

    iterations = int(v_len / step)

    l = []
    for i in range(iterations):
        o = get_x_vector_axis(v_len, function, step * i)
        l.append(o)
    return l


def run_this(function, q_vector, limit_d, limit_u, step, plot_name):
    start = timer()

    len_q = len(q_vector)
    x_vectors_list = get_offset_x_vector_list(len_q, function, step=step)

    results = [(0, 0), (0, 0), (0, 0)]
    # results = []
    for j, x_vectors in enumerate(x_vectors_list):
        for i, x in enumerate(x_vectors):
            corref = np.corrcoef(q_vector, x)[0][1]
            results.append((corref, i * len_q + (j * step)))
            if corref == 1:
                break
        else:
            continue
        break
    results.sort(reverse=True, key=lambda o: o[0])

    stop = timer()
    q_range = range(limit_d, limit_u)

    # p1 = (range(len(function)), np.zeros(shape=(len(function),)))
    # p2 = (q_range, np.full(shape=(limit_u - limit_d), fill_value=2))
    p3 = (range(results[0][1], results[0][1] + len_q), np.full(shape=len_q, fill_value=1.5), results[0][0])
    # p4 = (range(results[1][1], results[1][1] + len_q), np.full(shape=len_q, fill_value=1.3), results[1][0])
    # p5 = (range(results[2][1], results[2][1] + len_q), np.full(shape=len_q, fill_value=1.1), results[2][0])

    b1 = np.intersect1d(p3[0], q_range)
    overlap = 0
    if b1.all() != None:
        for b in b1:
            if b:
                overlap += 1

    overlap *= 100 / len_q

    # if overlap > 90:
    #     plt.clf()
    #     plt.figure(figsize=(18, 5))
    #     plt.title(f"STEPS: {step} -- TIME: {stop - start}")
    #     plt.plot(p1[0], p1[1], "b-")
    #     plt.plot(p2[0], p2[1], "r-")
    #     plt.plot(p3[0], p3[1], "y-")
    #     plt.plot(p4[0], p4[1], "black")
    #     plt.plot(p5[0], p5[1], "pink")
    #     plt.legend(["Main", "Q", p3[2], p4[2], p5[2]])
    #     plt.savefig(plot_name)
    return results[0], overlap, stop - start
