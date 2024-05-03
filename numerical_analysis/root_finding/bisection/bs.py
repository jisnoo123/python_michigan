#Bisection Method of Root Finding

def f(x):
    return x**3-x-1

a=1
b=2
tol=1e-6
err=tol+1
itr=0
c=0
while err>tol:
    itr+=1
    c=(a+b)/2
    if(f(c)==0):
        print('Root is:',c)
        break
    elif(f(a)*f(c)>0):
        a=c
    else:
        b=c
    err=abs(b-a)

print('Result is:',c)