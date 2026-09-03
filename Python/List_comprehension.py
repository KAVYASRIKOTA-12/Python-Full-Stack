#list comprehension
#every list comprehension can be rewritten as a for loop but every for loop cannot be rewritten in list comprehension.
'''a=["python","codegnan","course"]
#print(a.upper())#error
b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

'''a=["vja","hyd","vzg"]
#["Vja","Hyd","Vzg"]
b=[i.title() for i in a]
print(b)'''

'''a=["PYTHON","JAVA","DSA"]
b=[i.lower() for i in a]
print(b)'''

'''a=[2,3,4,5,6,8,12,13]
#[4,9,16,25,36,64,144,169]
b=[i**2 for i in a]
b=[i*i for i in a]
b=[pow(i,2) for i in a]
print(b)'''

#if usage in list  comprehension
'''for i in range(16):
    print(a)'''

'''a=[i for i in range(21) if i%2==0]
print(a)'''

'''a=[i*i for i in range(21) if i%2==0]
print(a)'''

'''fruits=["apple","banana","grapes","kiwi","mango","berry"]
a=[i for i in fruits if "a" in i] 
print(a)'''

'''fruits=["apple","banana","grapes","kiwi","mango","berries"]
a=[i for i in fruits if "a" not in i] 
print(a)'''

#no-elif usage in list comprehension

#if-else usage in list comprehesion
'''a=[i*i if i%2==0 else i*5 for i in range(31)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6]
c=[a[i]+b[i] for i in range(5)]
d=[a[i]+b[i] for i in range(len(a))]
print(c)'''
