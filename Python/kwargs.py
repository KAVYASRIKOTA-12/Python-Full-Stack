#kwargs    
'''def Details(**a):
    print(a)
    print(type(a))
Details()
d={"idnos":[10,20,30],
   "names":["bhanu","monali","rekha"],
   "status":["p","a","p"]}
Details(**d)'''

'''def Details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
Details()
d={"idnos":[10,20,30],
   "names":["bhanu","monali","rekha"],
   "status":["p","a","p"]}
Details(**d)'''

#both * and ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()    
d=(2,3,4,5.6,3.4)
final(*d)
e={"idnos":[10,20,30],
   "names":["bhanu","monali","rekha"],
   "status":["p","a","p"]}
final(**e)
final(*d,**e)'''
