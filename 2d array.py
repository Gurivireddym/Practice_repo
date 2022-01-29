
#from array import *
from numpy import *

a = matrix('1 2;4 5')
print(a)

b = a.flatten()
print(b)

c = b.reshape(1,4)
print(c)

print(a.max())

d = matrix('1 0;0 1')
print(d)
e = a * d;
print(e)


