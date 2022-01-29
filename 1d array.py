from array import *

a=array('i',[1,2,3,4,4,5,6])
b=array('u',['a','b','b'])

for i in a,b:
    print(i)
a.reverse()
print(a)

c = int(input('enter a number to search'))
print(a.index(c))

#Another way for getting Index of a searching element
k=0
for i in a:
    if i == c:
        print(k)
        break
    k +=1
    
