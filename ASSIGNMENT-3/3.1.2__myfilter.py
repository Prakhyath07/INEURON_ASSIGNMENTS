def myfilter(func,iterable):
    l=len(iterable)
    a=[]
    if func==None:
        for i in range(l):
            if bool(iterable[i])==True:
                a.append(iterable[i])
    else:

        for i in range(l):
            if func(iterable[i])==True:
                a.append(iterable[i])
    return iter(a)

