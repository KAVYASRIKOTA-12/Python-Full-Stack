Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
a={"name":"kavya","year":2025,"month":"may"}
print(a)
{'name': 'kavya', 'year': 2025, 'month': 'may'}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['kavya', 2025, 'may'])
a.items()
dict_items([('name', 'kavya'), ('year', 2025), ('month', 'may')])
a={"city":"vja","country":"india"}
a.update({"state":"ap"})
a
{'city': 'vja', 'country': 'india', 'state': 'ap'}
a.update({"state":"ap"},{"dist":"NTR"})
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.update({"state":"ap"},{"dist":"NTR"})
TypeError: update expected at most 1 argument, got 2
a.update({"state":"ap","dist":"NTR"})
a
{'city': 'vja', 'country': 'india', 'state': 'ap', 'dist': 'NTR'}
a={"day":"thursday","date":14}
a.setdefault("time",10)
10
a
{'day': 'thursday', 'date': 14, 'time': 10}
a={"name":"kavya","mailid":"kavya@gmail.com"}
a.get("name")
'kavya'
a
{'name': 'kavya', 'mailid': 'kavya@gmail.com'}
a["name"]
'kavya'
a["kavya"]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a["kavya"]
KeyError: 'kavya'
a.get("kavya")
a
{'name': 'kavya', 'mailid': 'kavya@gmail.com'}
a={"city":"vja","mobile no":12546,"mail id":"hjk@gmail.com"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("city")
'vja'
a.popitem()
('mail id', 'hjk@gmail.com')
a
{'mobile no': 12546}
a={"date":4,"month":6,"time":10}
a.copy()
{'date': 4, 'month': 6, 'time': 10}
a.clear()
>>> a
{}
>>> a={"date":4,"month":6,"time":10}
>>> len(a)
3
>>> a={"name":"kavya","city":"vja,"name":"kavya"}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> a={"name":"kavya","city":"vja","name":"kavya"}
...    
>>> print(a)
...    
{'name': 'kavya', 'city': 'vja'}
>>> a={"name":"kavya","city":"vja","name":"sri"}
...    
>>> print(a)
...    
{'name': 'sri', 'city': 'vja'}
>>> a={"name":"kavya","city":"vja","name1":"kavya"}
...    
>>> print(a)
...    
{'name': 'kavya', 'city': 'vja', 'name1': 'kavya'}
>>> a={"idnos":[10,20,30],"names":["kavya","sri","harika"],"marks":[70,80,90]}
...    
>>> print(a)
...    
{'idnos': [10, 20, 30], 'names': ['kavya', 'sri', 'harika'], 'marks': [70, 80, 90]}
>>> a.keys()
...    
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
...    
dict_values([[10, 20, 30], ['kavya', 'sri', 'harika'], [70, 80, 90]])
>>> a.items()
...    
dict_items([('idnos', [10, 20, 30]), ('names', ['kavya', 'sri', 'harika']), ('marks', [70, 80, 90])])
