Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len
a="kavya sri"
len(a)
9
a="python cousre"
len(a)
13
a=" "
len(a)
1
a=""
len(a)
0
#count
a="jhonny jhonny yes papa"
a.count("jhonny")
2
a.count("n")
4
a.count
<built-in method count of str object at 0x0000022395BDF8B0>(
a.count("y")
3
#find a string
a="course"
a.find("r")
3
a.find("e")
5
#escape sequences
#\n->new line
#\t->tab space
a="name\nemailid\tmobile number"
print(a)
name
emailid	mobile number
b="name:kavya\nmailid:kavyasri@gmail.com\tmobileno:123456"
print(b)
name:kavya
mailid:kavyasri@gmail.com	mobileno:123456
#replace
a="wait untilyou succeed"
a.replace("wait","work")
'work untilyou succeed'
a="wait wait until you succeed"
a.replace("wait","work")
'work work until you succeed'
a.replace("wait","work",1)
'work wait until you succeed'
#upper
a="code"
a.upper()
'CODE'
a="PYTHON"
a.lower()
'python'
a="kavya"
capitalize()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    capitalize()
NameError: name 'capitalize' is not defined
a.capitalize()
'Kavya'
a="im in a class"
a.title()
'Im In A Class'
a.capitalize()
'Im in a class'
#True False
a="hello"
a.isupper()
False
a.islower()
True
a.isdigit()
False
b=2345
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b="2345"
b.isdigit()
True
b.isalpha()
False
a="kavya123"
a.isalnum()
True
>>> a="kavya@12"
>>> a.isalnum()
False
>>> c="python"
>>> c.startswith("p")
True
>>> c.startswith("w")
False
>>> c.endswith("n")
True
>>> c.endswith("q")
False
>>> #strip
>>> #lstrip
>>> #rstrip
>>> a="    kavya      "
>>> a.strip()
'kavya'
>>> a.lstrip()
'kavya      '
>>> a.rstrip()
'    kavya'
>>> a="      kavya sri     "
>>> a.strip()
'kavya sri'
>>> a.lstrip()
'kavya sri     '
>>> a.rstrip()
'      kavya sri'
>>> #split
>>> a="python java c c=+"
>>> a.split()
['python', 'java', 'c', 'c=+']
>>> a="pythonjava"
>>> a.split()
['pythonjava']
>>> a="im in class"
>>> a.split()
['im', 'in', 'class']
