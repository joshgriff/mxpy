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


def Rxx(X):
    R = np.zeros([X.shape[1],X.shape[1]])
    for i in range(X.shape[0]):
        for j in range(i,X.shape[0]):
            R += X[j,:].T@X[i,:]
    return(R)

def Rxx_gen(wg):
    for w in wg:
        yield(Rxx(w))








#
