Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: E:/pyprograms/palindrome.py ====================
palindrome
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
array('i', [1, 2, 3, 4, 5])
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
Traceback (most recent call last):
  File "E:/pyprograms/1d array.py", line 3, in <module>
    print(a.shape())
AttributeError: 'array.array' object has no attribute 'shape'
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
Traceback (most recent call last):
  File "E:/pyprograms/1d array.py", line 3, in <module>
    for i in arr:
NameError: name 'arr' is not defined
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
1
2
3
4
5
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
array('i', [1, 2, 3, 4, 5])
array('u', 'abb')
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
array('i', [1, 2, 3, 4, 5, 6])
array('u', 'abb')
>>> 
====================== RESTART: E:/pyprograms/1d arr.py ======================
enter how many numbeers you want to enter5
>>> 
====================== RESTART: E:/pyprograms/1d arr.py ======================
enter how many numbeers you want to enter4
enter  next number2
enter  next number4
enter  next number3
enter  next number5
>>> 
====================== RESTART: E:/pyprograms/1d arr.py ======================
enter how many numbeers you want to enter4
enter  next number4
enter  next number5
enter  next number25
enter  next number5
array('i', [4, 5, 25, 5])
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
array('i', [1, 2, 3, 4, 5, 6])
array('u', 'abb')
array('i', [6, 5, 4, 3, 2, 1])
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
array('i', [1, 2, 3, 4, 5, 6])
array('u', 'abb')
array('i', [6, 5, 4, 3, 2, 1])
enter a number to search4
2
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 1, in <module>
    a = array('i',[1,2,4,3,5,5,7,36,7])
NameError: name 'array' is not defined
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 4, in <module>
    a.shape(3,3)
AttributeError: 'array.array' object has no attribute 'shape'
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 3, in <module>
    a = matrix('1 2 3;4 4 5')
NameError: name 'matrix' is not defined
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2 3]
 [4 4 5]]
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2 3]
 [4 4 5]]
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 6, in <module>
    a.shape(1,6)
TypeError: 'tuple' object is not callable
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2 3]
 [4 4 5]]
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 6, in <module>
    b = a.shape(1,6)
TypeError: 'tuple' object is not callable
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2 3]
 [4 4 5]]
[[1 2 3 4 4 5]]
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2 3]
 [4 4 5]]
[[1 2 3 4 4 5]]
[[1 2]
 [3 4]
 [4 5]]
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2 3]
 [4 4 5]]
[[1 2 3 4 4 5]]
[[1 2]
 [3 4]
 [4 5]]
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 10, in <module>
    print(c.shape())
TypeError: 'tuple' object is not callable
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 5, in <module>
    print(z.shape())
TypeError: 'tuple' object is not callable
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2 3]
 [4 4 5]]
[[1 2 3 4 4 5]]
[[1 2]
 [3 4]
 [4 5]]
5
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2]
 [4 5]]
[[1 2 4 5]]
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 9, in <module>
    c = b.reshape(3,2)
ValueError: cannot reshape array of size 4 into shape (3,2)
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2]
 [4 5]]
[[1 2 4 5]]
5
[[1 0]
 [0 1]]
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2]
 [4 5]]
[[1 2 4 5]]
5
[[1 0]
 [0 1]]
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 15, in <module>
    e = a * b
  File "C:\Program Files\Python36\lib\site-packages\numpy\matrixlib\defmatrix.py", line 218, in __mul__
    return N.dot(self, asmatrix(other))
  File "<__array_function__ internals>", line 6, in dot
ValueError: shapes (2,2) and (1,4) not aligned: 2 (dim 1) != 1 (dim 0)
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2]
 [4 5]]
[[1 2 4 5]]
5
[[1 0]
 [0 1]]
Traceback (most recent call last):
  File "E:/pyprograms/2d array.py", line 15, in <module>
    e = a * b;
  File "C:\Program Files\Python36\lib\site-packages\numpy\matrixlib\defmatrix.py", line 218, in __mul__
    return N.dot(self, asmatrix(other))
  File "<__array_function__ internals>", line 6, in dot
ValueError: shapes (2,2) and (1,4) not aligned: 2 (dim 1) != 1 (dim 0)
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2]
 [4 5]]
[[1 2 4 5]]
5
[[1 0]
 [0 1]]
[[1 2]
 [4 5]]
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2]
 [4 5]]
[[1 2 4 5]]
5
[[1 0]
 [0 1]]
[[1 2]
 [4 5]]
>>> 
===================== RESTART: E:/pyprograms/2d array.py =====================
[[1 2]
 [4 5]]
[[1 2 4 5]]
[[1 2 4 5]]
5
[[1 0]
 [0 1]]
[[1 2]
 [4 5]]
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
array('i', [1, 2, 3, 4, 5, 6])
array('u', 'abb')
array('i', [6, 5, 4, 3, 2, 1])
enter a number to search3
3
3
>>> 
===================== RESTART: E:/pyprograms/1d array.py =====================
array('i', [1, 2, 3, 4, 4, 5, 6])
array('u', 'abb')
array('i', [6, 5, 4, 4, 3, 2, 1])
enter a number to search4
2
2
>>> 
