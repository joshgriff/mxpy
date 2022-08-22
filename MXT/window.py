#
import numpy as np

def window_gen(dg,N):
    D = np.zeros(N)
    for d in dg:
        D[:-1]  = D[1:]
        D[-1]   = d
        yield(D)

def window2_gen(dg,N,ND):
    D = np.zeros([N,ND])
    for d in dg:
        D[:-1,:] = D[1:,:]
        D[-1,:] = d
        yield(D)























#
