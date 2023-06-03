fname= input('Enter a file ')
fhand=open(fname)
l=list()

c=0
for i in fhand:
    i = i.rstrip()
    if i.startswith('From '):
        c=c+1
        words = i.split()
        w=words[1]
        print(w)
print('There were',c,'lines in the file with From as the first word')