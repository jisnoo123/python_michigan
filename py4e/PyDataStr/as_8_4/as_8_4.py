fname=input('enter a file ')
fhand=open(fname)
l=list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        print('Word',word)
        if word not in l:
            l.append(word)
            print('List: ', l)
l.sort()
print(l)