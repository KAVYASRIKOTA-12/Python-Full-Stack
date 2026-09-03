#global and local variables
#variables inside and outside the function is called global and local variables.
#A variable defined above the function and is acessible to the entire global space is called global variable.
#A variable is defined inside the function is called local variable.

#first case of global variable
'''a=3
def check():
    print("inside the value is",a)
check()
print("outside the value is",a)'''

#second case of global variable
'''a=2
def check1():
    a=5
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)'''

#third case of both local and global variable
'''a=4
b=9
def check2():
    a=3
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is ",b)'''

#usage of global keyword
#when user wants to access the global variable inside the function directly and carry forward the updated value even outside the function then we use global keyword.

#final case of both global and local variable
'''a=4
def final():
    global a,b
    print("inside the value is",a)
    a=5
    print("updated value is",a)
    b=13
    b=b+a
    print("b value is",b)
final()
print("a value is",a)
print("b value is",b)'''
