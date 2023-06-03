fname = input('Enter a file name ')
fhand = open(fname)
di=dict()
for lin in fhand:
    lin = lin.rstrip()
    wds=lin.split()
    for w in wds:
        if w in di:
            di[w]= di[w]+1
        else:
            di[w]=1
print(di)