#generators
#no tuple comprehension in above cases if we remove those braces and keep paranthesis then the outcome is generators.
#syntax
#a=(expr for var in collection/range)

'''a=(i for i in range(16))
print(*a)
print(type(a))'''
#print(list(a))
#print(tuple(a))
#print(set(a))

#a generator is also a function which can be used as an iterator{loop} by producing group of values,where we use yield keyword.
#yield vs return
#return will terminate the function where as yield can pass the function and go on with every succesive iteration.

'''a,b=[int(x) for x in input("enter the values").split(",")]
def data(a,b):
    while a<b:
        a=a+1
        yield a
print(*data(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def data(a,b):
    while a<b:
        a=a+1
        return a
print(data(a,b))'''
