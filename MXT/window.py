#
import numpy as np

def window_gen(dg,N):
    D = np.zeros(N)
    for d in dg:
        D[:-1]  = D[1:]
        D[-1]   = d
        yield(D)

























#
