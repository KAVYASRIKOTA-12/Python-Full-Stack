Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #int
>>> int(8)
8
>>> int(5.7)
5
>>> int('kavya')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('kavya')
ValueError: invalid literal for int() with base 10: 'kavya'
>>> int(4=8j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> int(True)
1
>>> int(False)
0
>>> #float
>>> flaot(3)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    flaot(3)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
>>> float(3.7)
3.7
>>> float('kavya')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float('kavya')
ValueError: could not convert string to float: 'kavya'
>>> float(4+6j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(4+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #str
>>> str(5)
'5'
>>> str(3.9)
'3.9'
>>> str('kavya')
'kavya'
str(4+9j)
'(4+9j)'
str(True)
'True'
str(False)
'False'
#complex
complex(3)
(3+0j)
complex(4.9)
(4.9+0j)
complex(5+2j)
(5+2j)
complex('kavya')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex('kavya')
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
#bool
bool(9)
True
bool(3.9)
True
bool('kavya')
True
bool(5+9j)
True
bool(True)
True
bool(False)
False
