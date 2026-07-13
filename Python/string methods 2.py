Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=2
>>> b=3
>>> print("".format(a*b))

>>> mul(a,b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    mul(a,b)
NameError: name 'mul' is not defined
>>> print(f"the product is".format(a*b))
the product is
>>> print("the product is{}".format(a*b))
the product is6
>>> print(f"the product is {c}".format(a*b))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(f"the product is {c}".format(a*b))
NameError: name 'c' is not defined
>>> print(f"the product is {a*b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"the product is {a*b}")
...       
the product is 6
>>> c=a*b
...       
>>> print("the product is {}".format(c})
...       
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> print("the product is {}".format(c))
...       
the product is 6
>>> print(f"the product is {c}")
...       
the product is 6
