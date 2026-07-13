Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#join()
a="python","java","c"
"".join(a)
'pythonjavac'
" ".join(a)
'python java c'
#formatting
a=10
b=20
print(a+b)
30
print("the sum is",a)
the sum is 10
a="vja"
print("the city is",a)
the city is vja
print("the city is,a")
the city is,a
#concatenation
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="kavya"
lname="kota"
print(fname+lname)
kavyakota
>>> print(fname+" "+lname)
kavya kota
>>> print(fname.title()+" "+lname.title())
Kavya Kota
>>> print((fname+" "+lname).title())
Kavya Kota
>>> #format method
>>> a="motu"
>>> b="patlu"
>>> print("hello {}{}".format(a+b))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print("hello {}{}".format(a+b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello{}".format(a,b))
hello motu hellopatlu
>>> print
<built-in function print>
>>> print("hello {} \n hello {}".format(a,b))
hello motu 
 hello patlu
>>> #fstring
...  
>>> a="micky"
>>> b="mouse"
>>> print(f"hello {a}{b}")
hello mickymouse
>>> print(f"hello {a} {b}")
hello micky mouse
>>> print(f"hello {a} hello{b}")
hello micky hellomouse
>>> print(f"hello {a} \nhello {b}")
hello micky 
hello mouse
