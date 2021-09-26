def myreduce(func,iterable,initializer=None):
    l=len(iterable)-1
    if initializer==None:
        a=iterable[0]
        for i in range(l):
            b=iterable[i+1]
            a=func(a,b)
    else:
        a=initializer
        for i in range(l):
            b=iterable[i]
            a=func(a,b)

    return a






