Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthmetic
a=2
b=8
print(a+b)
10
print(a-b)
-6
print(a//b)
0
print(a/b)
0.25
print(a*b)
16
print(a**b)
256
print(a%b)
2
#asignment
a=2
b=4
b+=a
b
6
b-=1
b
5
b//=2
b
2
b/=1
b
2.0
b*=3
b
6.0
b**=2
b
36.0
b%=4
b
0.0
print(a+=b)
SyntaxError: invalid syntax
#comparision
a=2
b=4
a<b
True
b>a
True
a<=b
True
b>=a
True
a>b
False
b>a
True
b<a
False
a==b
False
a=3
b=3
a==b
True
a!=b
False
#logical
a=6
b=9
a<b and b>a
True
a<=b and b>=a
True
>>> a!=b and b!=a
True
>>> a<=b or b>=a
True
>>> a>=b or b<=a
False
>>> a!=b or b!=a
True
>>> not True
False
>>> not false
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    not false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> not False
True
>>> #identify
>>> a=6
>>> if type(a) is not int:
...     print("it is int")
... 
...     
>>> if type(a) is int:
...     print("it is int")
... 
...     
it is int
>>> #membership
>>> a=1,2,3,4,5,6,7,8
>>> if 4 in a:
...     print(4)
... 
...     
4
>>> if 9 in a:
...     print(9)
... 
...     
>>> if 10 not in a:
...     print(10)
... 
...     
10
>>> #bitwise
