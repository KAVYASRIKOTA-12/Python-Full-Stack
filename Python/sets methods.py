Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #sets
>>> a={4,5.6,"python",2+9j,True,False}
>>> print(a)
{False, True, 4, 5.6, 'python', (2+9j)}
>>> type(a)
<class 'set'>
>>> a={1,2,3,4,5,6,7,8}
>>> b={6,7,8}
>>> b.issubset (a)
True
>>> a.issubset (b)
False
>>> a={1,2,3,4,6,6,7,8,7,8}
>>> print(a)
{1, 2, 3, 4, 6, 7, 8}
>>> a={9,8,6,4,5,3,2}
>>> b={6,4,5}
>>> a.issuperset (b)
True
>>> b.issuperset(a)
False
>>> a={1,2,3,4,5,6,7}
>>> a.add(8)
>>> print(a)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> #union
>>> a={5,6,7,8,9,10}
>>> b={11,12,13,14,15}
>>> a.union(b)
{5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
>>> b.union(a)
{5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
>>> a={11,12,13,14,15}
>>> b={14,15,16,17,18}
>>> a.intersection(b)
{14, 15}
>>> b.intersection(a)
{14, 15}
#update
a={5,6,7,8,9,10}
b={8,9,10,11,12}
a.update(a)
a.update(b)
a
{5, 6, 7, 8, 9, 10, 11, 12}
b
{8, 9, 10, 11, 12}
a
{5, 6, 7, 8, 9, 10, 11, 12}
b.update(a)
b
{5, 6, 7, 8, 9, 10, 11, 12}
#difference
a={4,5,6,7,8}
b={1,2,3,4,5}
a.difference(b)
{8, 6, 7}
b.difference(a)
{1, 2, 3}
#
#symmetric
a={3,4,5,6,7,8}
b={6,7,8,9,10}
a.symmetric_difference(b)
{3, 4, 5, 9, 10}
b.symmetric_difference(a)
{3, 4, 5, 9, 10}
#difference update
a={5,6,7,8,9,10}
b={8,9,10,11,12}
a.difference_update(b)
a
{5, 6, 7}
b
{8, 9, 10, 11, 12}
b.difference_update(a)
b
{8, 9, 10, 11, 12}
#intersection update
a={4,5,6,7,8,9}
b={1,2,3,4,5,6}
a.intersection_update(b)
a
{4, 5, 6}
b
{1, 2, 3, 4, 5, 6}
b.intersection_update(a)
b
{4, 5, 6}
#symmetric difference update
a={3,4,5,6,7,8}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8}
b
{1, 2, 3, 4, 5, 6}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8}
#copy
a={10,20,30,40,50}
a.copy()
{50, 20, 40, 10, 30}
#clear
a={10,20,30,40}
a.clear()
a.add(20)
a
{20}
a.clear()
a
set()
a.add
<built-in method add of set object at 0x000001D64D332960>
a.add(90,100)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.add(90,100)
TypeError: set.add() takes exactly one argument (2 given)
#pop
a=(7,8,9,10,11}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
a={7,8,9,10,11}
a.pop()
7
a.pop(8)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.pop(8)
TypeError: set.pop() takes no arguments (1 given)
a.remove(10)
a
{8, 9, 11}
#discard
a={1,2,3,4,5,6}
a.discard(5)
a
{1, 2, 3, 4, 6}
b={2,3,4,5,6,7}
c={7,8,9,10}
b.discard(c)
b
{2, 3, 4, 5, 6, 7}
c
{8, 9, 10, 7}
#len
a={5,6,7,8,9}
len(a)
5
a.count(8)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.count(8)
AttributeError: 'set' object has no attribute 'count'
a.index(5)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.index(5)
AttributeError: 'set' object has no attribute 'index'
#disjoint
a={1,2,3,4,5,6}
b={4,5,6,7,8}
a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
a={1,2,3,4,5,6}
b={8,9,10}
a.isdisjoint(b)
True
