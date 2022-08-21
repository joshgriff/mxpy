import numpy as np

def ewma_gen(dg,f):
    ld = dg.__next__()
    ly = ld
    for d in dg:
        y = (f)*d+(1-f)*ly
        ly = y
        yield(y)


