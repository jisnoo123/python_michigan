fname = input('Enter file name')
fhand= open(fname)
l = list()
for thing in fhand:
    if thing.startswith('X-DSPAM-Confidence:'):
        pos = thing.split()
        d = pos[1]
        d=float(d)
        l.append(d)

print('Average spam confidence:',sum(l)/len(l))
