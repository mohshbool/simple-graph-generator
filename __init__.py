import matplotlib.pyplot as plt
import numpy as np


def generateBarGraph(data, title):
    ndata = np.array(data)
    speeds = np.vectorize(lambda s: s["speed"])(ndata)
    unique, counts = np.unique(speeds, return_counts=True)
    p = plt.bar(
        unique,
        counts,
        0.01
    )
    plt.ylabel = 'Number of Elements'
    plt.title = title
    plt.xticks(
        unique,
        unique,
    )
    plt.yticks([ndata.size], [ndata.size])
    plt.legend(p)
    return p
