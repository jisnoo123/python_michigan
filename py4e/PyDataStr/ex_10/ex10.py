fname=input('Enter a file ')
fhand = open(fname)
d=dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        #making the histogram 
        d[word]=d.get(word,0)+1
l=list()
for k,v in d.items():
    l.append((v,k))
l=sorted(l,reverse=True)
#printing in anice manner
for v,k in l[:5]:
    print(k,v)
