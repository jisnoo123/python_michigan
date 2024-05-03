#Simposn's 1/3rd program

a=int(input('Enter lower limit:'))
b=int(input('Enter upper limit:'))
n=int(input('Enter number of intervals:'))
h=(b-a)/n
def f(x):
    return x
I=f(a)+f(b)

for i in range (1,n):
    if(i%2==0):
        I=I+2*f(a+i*h)
    else:
        I=I+4*f(a+i*h)

result=(I*h)/3
print('Integration result:',result)