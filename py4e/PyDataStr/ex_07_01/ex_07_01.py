fname = input("enter file")
fhand = open(fname)
for thing in fhand:
    print(thing.upper())