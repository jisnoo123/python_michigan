#Trapezoidal composite method to find area under the curve

a=int(input('Enter lower limit of integration:'))
b=int(input('Enter upper limit of integration:'))
n=int(input('Enter No. of partitions:'))
h=(b-a)/n

def f(x):
    return x**2-1

sum_in=0
for i in range(n-1):
    sum_in+=f(a+(i+1)*h)

sum_in=2*sum_in
sum_bound=f(a)+f(b)

area=h*(sum_bound+sum_in)/2
print('Area under the curve:',abs(area))