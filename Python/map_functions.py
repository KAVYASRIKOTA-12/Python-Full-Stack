#map function->each object from a collection and forms a new collection.
'''a=[2,6,8,9,10,20,5,60]
b=[1,4,7,12,14,70,80,90]
c=list(map(max,a,b))
print(c)'''

'''a=[2,6,8,9,10,20,5,60]
b=[1,4,7,12,14,70,80,90]
c=list(map(min,a,b))
print(c)'''

#split and map
'''a=input("data 1")
b=input("data 2")
print(a+b)'''

'''a,b=input("enter the values").split(","))
pint(a+b)'''

'''a,b=[x for x in input("data").split(",")]
print(a+b)'''

'''a,b=map(str,input("enter the names").split(",")))]
print(a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=int(input("enter the values").split(","))
print(a+b)'''   #error

'''a,b=[int(x) for x in input("enter the values").split(",")]
print(a+b)'''

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a=tuple(map(int,input("enter the values").split(",")))
print(a)'''

'''a=list(map(int,input("enter the values").split(",")))
print(a)'''

'''a=set(map(int,input("enter the values").split(",")))
print(a)'''

'''a=list(map(str,input("enter the values").split(",")))
print(a)'''

'''a=list(map(eval,input("enter the values").split(",")))
print(a)'''

'''a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''
