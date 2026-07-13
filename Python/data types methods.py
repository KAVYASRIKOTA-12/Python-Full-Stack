Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,3.8,"kavya",7+8j,True,False]
print(a)
[3, 3.8, 'kavya', (7+8j), True, False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
b=[8.9]
type(b)
<class 'list'>
#append
a=["python","java","c++"]
a.append("ml")
print(a)
['python', 'java', 'c++', 'ml']
a.append("c","sql")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("c","sql")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["c","sql"])
print(a)
['python', 'java', 'c++', 'ml', ['c', 'sql']]
#extend
a=["apple","banana"]
a.extend(["mango","grapes"])
print(a)
['apple', 'banana', 'mango', 'grapes']
#insert
a=["black","white","red"]
a.insert(1,"pink")
print(a)
['black', 'pink', 'white', 'red']
#index
a=["ml","ai","ds"]
a.index("ds")
2
a.copy()
['ml', 'ai', 'ds']
b=a.copy()
b
['ml', 'ai', 'ds']
a
['ml', 'ai', 'ds']
a["yellow","green","red"]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a["yellow","green","red"]
TypeError: list indices must be integers or slices, not tuple
a=["yellow","green","red"]
a.sort()
a
['green', 'red', 'yellow']
a=[2,0,8,56,98,67]
a.sort()
a
[0, 2, 8, 56, 67, 98]
#reverse
a=["vja","hyd","vzg"]
a.reverse()
a
['vzg', 'hyd', 'vja']
a=[3,2,5,6,7,8]
a.reverse()
a
[8, 7, 6, 5, 2, 3]
#pop
a=["python","java","c","ml"]
a.pop()
'ml'
a.pop(1)
'java'
a
['python', 'c']
#remove
a=["python","ml","c"]
a.remove("ml")
a
['python', 'c']
#len
a=["hi","hello","how"]
len(a)
3
b="hello"
len(b)
5
>>> c=["hello"]
>>> len(c)
1
>>> a.count("hello")
1
>>> #clear
>>> a=["python","java","c"]
>>> a.clear()
>>> a
[]
>>> a.append("kavya")
>>> a
['kavya']
>>> a.extend("sri","kota")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.extend("sri","kota")
TypeError: list.extend() takes exactly one argument (2 given)
>>> a.extend(["sri","kota"])
>>> a
['kavya', 'sri', 'kota']
>>> #tuple()
>>> a=(5,9.7,"kavya",6+9j,True,False)
>>> print(a)
(5, 9.7, 'kavya', (6+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> len(a)
6
>>> count("True")
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    count("True")
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count(True)
1
>>> a.index("kavya")
2
