#functions
#a function is a block of organized,reusable code and that is used to perform a single or multiple tasks.
#python gives inbulit functions like print,you can make your own function also and this are called userdefined functions.
#functions blocks begin with the keyword def followed by the function name and paranthesis(()).
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

'''def calculate(a,b):
  print("the sum is",a+b)
  print("the diff is",a-b)
  print("the product is",a*b)
calculate(10,20)  
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
  print(a//b)
  print(a**b)
  print(a%b)
calculate(20,30)'''

'''def add(a,b):
  print(a+b)
add(2,5)'''

'''while True:
  def add():
    a=int(input())
    b=int(input())
    print(a+b)
  add()'''

'''def add():
  a=int(input("a value"))
  b=int(input("b value"))
  print(a+b)
  add()
add()'''

'''def fullname():
  fname=input("first name")
  lname=input("last name")
  print((fname+" "+lname).title())
fullname()'''

#print just shows the humanuser input in a console.
#return will terminate the function and give back a value from the function.
'''def calculate():
  a=int(input())
  b=int(input())
  option=input("enter the option: 1.add 2.diff 3.product")
  if option==1:
    print(a+b)
  elif option==2:
    print(a-b)
  elif option==3:
    print(a*b)
  else:
      print("Invalid option")
calculate()'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input())
    b=int(input())
    option=input("enter the option: 1.add 2.diff 3.product")
    if option=="1":
        add()
    elif option=="2":
        sub()
    elif option=="3":
        mul()'''   

'''while True:
  def splitbill():
    a=int(input())
    b=int(input())
    print("perhead:",b//a)
  splitbill()'''

'''def splitbill():
    a=int(input())
    b=int(input())
    print("perhead:".format(b//a))
    print(f"perhead:{b//a})
splitbill()'''

'''def splitbill():
    a=int(input())
    b=int(input())
    c=b//a
    print("perhead:{}".format(c))
    print(f"perhead:{c}")
splitbill()'''
'''n=4
for i in range(n,0,-1):
    for j in range(n-i+1):
        print(j,end=" ")
    print()'''

#print vs return
'''def add(a,b):
    print(a+b)
add(4,5)'''

'''def add(a,b):
    return(a+b)
print(add(2,3))'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(4,5)'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(add(2,4))'''
