#
import numpy as np

def impulse_train_gen(A,N):
    i = 0
    while 1:
        if i%N==0:
            yield(1.0*A)
        else:
            yield(0)
        i+=1


def sin_gen(f,A,fs):
    t = 0
    dt = 1/fs
    while 1:
        yield(A*np.sin(f*t))
        t+=dt


def Rxx(X):
    R = np.zeros([X.shape[1],X.shape[1]])
    for i in range(X.shape[0]):
        for j in range(i,X.shape[0]):
            R += X[j,:][:,None]@X[i,:][:,None].T
    return(R/X.shape[0])

def Rxx_gen(wg):
    for w in wg:
        yield(Rxx(w))








#
