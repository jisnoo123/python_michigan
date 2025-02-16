import re
fname= input('Enter file name ')
fhand= open(fname)
#sum is s
s=0
for line in fhand:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    for num in nums:
        s = s+int(num)
#displaying the sum
print('The sum is:',s)