#Solving differential equation using Forward Euler Method
def f(x,y):
    return -5*y

x0=int(input('Enter x0:'))
y0=int(input('Enter y0:'))
n=int(input('Enter n:'))
xn=int(input('Enter x value at n:'))
h=(xn-x0)/n
x=[x0]
y=[y0]

for i in range(n):
    y_new=y[i]+h*f(x[i],y[i])
    x_new=x[i]+h
    x.append(x_new)
    y.append(y_new)

print('Result: y value at ',n,' is:',y[-1])