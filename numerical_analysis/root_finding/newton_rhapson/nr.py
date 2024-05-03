#Newton Rhapson

def f(x):
    return x**3-x-1

def df(x):
    return 3*x**2-1

tol=1e-6
err=tol+1
x=2
itr=0
while err>tol:
    itr+=1
    xn=x-(f(x))/(df(x))
    err=abs(x-xn)
    x=xn

print('Root is:',x)