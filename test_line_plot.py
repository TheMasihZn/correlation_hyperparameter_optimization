import librosa
import numpy as np
import matplotlib.pyplot as plt

def get_offset_x_vector_list(v_len, function, step=10):
    def get_x_vector_axis(v_len, function, offset=0):
        x_v_ax = []
        for i in range(int(len(function) / v_len)):
            lesser_lim = (i * v_len) + offset
            upper_lim = ((i + 1) * v_len) + offset
            if upper_lim <= len(function):
                x_v_ax.append(function[lesser_lim:upper_lim])

        return np.array(x_v_ax)


    iterations = int(v_len / step)

    l = []
    for i in range(iterations):
        o = get_x_vector_axis(v_len, function,i)
        l.append(o)
    return l


def run_this(function, q_vector, limit_d, limit_u, step):
    len_q = len(q_vector)

    x_vectors_list = get_offset_x_vector_list(len_q, function, step=step)
    plt.figure(figsize=(18, 5))
    for j, x_vectors in enumerate(x_vectors_list):
        if j == 100:
            for i, x in enumerate(x_vectors):
                plt.plot(x, np.full(shape=len_q, fill_value=(111 - i)))


    return plt

scale, sr = librosa.load("audio/scale.wav")
step = 100
limitD = 100010
limitU = 111250
q_vector = scale[limitD: limitU]

plot = run_this(range(len(scale)), q_vector, limitD, limitU, step)
plot.show()


