from array import *


a = array('i',[])
n = int(input('enter how many numbeers you want to enter'))

for i in range(n):
    b = int(input('enter  next number'))
    a.append(b)

print(a)
