#Anonymous function->are nameless functions and we use a keyword called as lambda to create anonymous functions.
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input("a value"))
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''

#tasks
'''a="codegnan"
b=lambda a:a.upper()
print(b(a))'''

'''a="python course"
b=lambda a:a.title()
print(b(a))'''


'''a=int(input("a value"))
b=int(input("b value"))
c=lambda a,b:a*b 
print(c(a,b))'''

'''fname=input("first name")
lname=input("last name")
a=lambda fname,lname:fname+" "+lname
print(a(fname,lname))'''

#using generator and anonumous functions
'''a,b=[x for x in input("enter the values").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''   #Codegnan

'''a=[2,8,10,13,15,17,20,23,25,50,80,90,100]
for i in a:
    if i%2==0:
        print(i)'''

#using filter()
'''a=[2,8,10,13,15,17,20,23,25,50,80,90,100]
b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],(),set(),{},None,"",4,6.7,"python",4+9j,True,False]
b=list(filter(None,a))
print(b)'''

#ATM application for different users
'''acc=10000
while True:
    card=(input("insert the card"))
    if card=="c":
        print("welcome kavya")
        password=int(input("enter the password"))
        if password==1234:
            option=int(input("enter the option 1.bal enq 2.withdraw"))
            if option==1:
                print(acc)
            elif option==2:
                    money=int(input("enter the money"))
                    print(money)
                    balance=acc-money
                    print("remaining bal is",balance)
            else:
                print("invalid option")
        else:
            print("incorrect password")
acc=2000
while True:
   elif card=="d":'''
