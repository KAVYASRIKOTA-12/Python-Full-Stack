Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0]
'c'
=
>>> a[0]
'c'
>>> 
>>> a[0]+a[1]+a[2]+a[3]
'code'
>>> a[0:3]
'cod'
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a="work until you succed"
>>> a[6:11]
'ntil '
>>> a[5:10]
'until'
>>> a[0:4]
'work'
>>> a[12:15]
'ou '
>>> a[11:14]
'you'
>>> a[15:21]
'succed'
>>> b="codegnan it solutions"
>>> b[10:11]
't'
>>> b[9:10]
'i'
b[9:11]
'it'
b[4:9]
'gnan '
a="I am learning python"
a[-15:-10]
'learn'
a[-6:-1]
'pytho'
b="I love python"
b[-11:-7]
'love'
b[-6:0]
''
b[-6:-1]
'pytho'
b[-6:1]
''
b[-6:-0]
''
b[-6:]
'python'
