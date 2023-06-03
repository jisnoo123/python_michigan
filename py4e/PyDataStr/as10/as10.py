fname=input('Enter a file ')
fhand=open(fname)
l=list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From ')  :
        words = line.split()
        hr =words[5]
        l.append(hr)
#list them for hours
hrs=list()
for h in l:
    Hour=h.split(':')
    h1=Hour[0]
    hrs.append(h1)
d=dict()
for h in hrs:
    #making the histogram
    d[h]=d.get(h,0)+1
#making a list of tuples
tup=list()
for k,v in d.items():
    newt=(k,v)
    tup.append(newt)
tup.sort()
#displaying nicely
for k,v in tup:
    print(k,v)