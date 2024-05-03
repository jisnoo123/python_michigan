x=list()
y=list()
n=int(input('Enter number of data sets:'))

for i in range(n):
    xn=float(input('Enter x:'))
    yn=float(input('Enter y:'))
    x.append(xn)
    y.append(yn)

sx=0
sy=0
sxy=0
sxsq=0

for i in range(n):
    sx+=x[i]
    sy+=y[i]
    sxsq+=x[i]*x[i]
    sxy+=x[i]*y[i]

m=(sx*sy-n*(sxy))/((sx*sx)-n*(sxsq))
c=(sy-m*sx)/n

print('Regression Line: y=',m,'x+',c)