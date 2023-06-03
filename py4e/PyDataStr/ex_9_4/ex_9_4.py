fname = input('Enter file name: ')
fhand=open(fname)
d=dict()
l=list()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        wds= line.split()
        w=wds[1]
        l.append(w)
    
#making histogram
for ea in l:
    d[ea]=d.get(ea,0)+1
largeval=-1
largeword=None
for k,v in d.items():
    if v>largeval:
        largeval=v
        largeword=k
print(largeword,largeval)