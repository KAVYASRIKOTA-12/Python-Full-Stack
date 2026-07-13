'''a=str(input("value"))
if type(a) is str:
    print("true")
else:
    print("false")'''

#if -condition by using comparision operators
#<,>,<=,>=,!=.==
'''a=10
if a>1:
    print("true")'''
'''a=10
if a<1:
    print("true")'''
'''a=10
if a==10:
    print("true")'''
'''a=int(input("a value"))
if a>20:
    print("greater")'''
'''a=int(input("a value"))
if a<20:
    print("greater")'''
'''a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("greater")'''

'''a=49
b=10
if a<b:
    print("greater")'''
'''a=10
b=10
if a==b:
    print("equal")'''
'''a=20
b=10
if a==b:
    print("equal")'''
'''a="python"
b="java"
if a!=b:
    print("not equal")'''
'''a=int(input("a value"))
if a!=20:
    print("greater")'''

#if-condition by using logical opertors
#and,or,not
'''a=3
b=4
if a<b and b>a:
    print("true")'''
'''a=3
b=4
if a<b or b>a:
    print("true")'''
'''a=7
b=4
if a>b or b<a:
    print("true")'''
'''a=8
b=5
if a!=b and b==a:
    print("true")'''
'''a=3
b=4
if a<=b or b>=a:
    print("true")'''
'''a=3
b=4
if not a>b and b<a:
    print("true")'''
'''a=3
b=4
if not a<b or b>a:
    print("true")'''
'''a=3
b=4
if not a==b or b!=a:
    print("true")'''
#if-condition by using identify operators
#is,is not
'''a=2
if type(a) is int:
    print("true")'''
'''a=2
if type(a) is not int:
    print("true")'''
'''a=int(input("a value"))
if type(a) is int:
    print("it is int")'''
'''a=int(input("a value"))
if type(a) is not int:
    print("it is int")'''
'''a=float(input("a value"))
if type(a) is float:
    print("it is int")'''
'''a=str(input("a value"))
if type(a) is str:
    print("it is str")'''
'''a=bool(input("a value"))
if type(a) is bool:
    print("it is bool")'''
'''a=bool(input("a value"))
if type(a) is not bool:
    print("it is bool")'''
#if-condition by using membership operators
#in,not in
'''a=[10,20,30,40,50]
if 40 in a:
    print("true")'''
'''a=[10,20,30,40,50]
if 40 not in a:
    print("true")'''
'''a=[10,20,30,40,50]
if 10 not in a:
    print("false")'''
'''a=[10,20,30,40,50]
b=int(input("value"))
if b in a:
    print("true")'''

'''a=int(input("value"))
if 50 in a:
    print("true")'''#error

#if-else conditions by using comparision
'''a=20
b=40
if a>b:
    print("true")
else:
    print("false")'''
'''a=20
b=40
if a!=b:
    print("true")
else:
    print("false")'''
'''a=20
b=40
if a==b:
    print("true")
else:
    print("false")'''
'''a=int(input("value"))
b=int(input("value"))
if a>b:
    print("true")
else:
    print("false")'''
#if-else condition by using membership operators
'''a=[10,20,30,40,50]
if 50 in a:
    print("true")
else:
    print("false")'''
'''a=[10,20,30,40,50]
if 60 in a:
    print("true")
else:
    print("false")'''
'''a=[10,20,30,40,50]
b=int(input("value"))
if 60 in a:
    print("true")
else:
    print("false")'''
'''a=[10,20,30,40,50]
if 60 in a:
    print("true")
else:
    print("false")'''
#if-else condition by using identity operators 
'''a=30
if type(a) is int:
    print("true")
else:
    print("false")'''
'''a=30
if type(a) is  not int:
    print("true")
else:
    print("false")'''

'''a=int(input("value"))
if type(a) is int:
    print("true")
else:
    print("false")'''
'''a=str(input("value"))
if type(a) is str:
    print("true")
else:
    print("false")'''
'''a=str(input("value"))
if type(a) is not str:
    print("true")
else:
    print("false")'''


#if-elif-else conditions by using comparision operators
'''a=10
b=20
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("false")'''
'''a=10
b=20
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("false")'''
'''a=10
b=20
if a<=b:
    print("less")
elif b>=a:
    print("greater")
elif a!=b:
    print("not equal")
elif a==b:
    print("equal")
else:
    print("false")'''
#if-elif-else conditions by using identify operators
'''a=70
if type(a) is int:
    print("it is int")
elif type(a) is not int:
    print("not int")
else:
    print("false")'''
'''a="kavya"
if type(a) is int:
    print("it is int")
elif type(a) is not int:
    print("not int")
else:
    print("false")'''
#if-elif-else conditions by using membership operators
'''a=[10,20,30,40,50]
if 50 in a:
    print("true")
elif 60 in a:
    print("no")
else:
    print("false")'''
'''a=[10,20,30,40,50]
if 60 in a:
    print("true")
elif 50 in a:
    print("no")
else:
    print("false")'''
#if-elif-else conditions by using logical operators
'''a=50
b=60
if a>b and b<a:
    print("true")
elif a<b or b!=a:
    print("yes")
else:
    print("false")'''

#multiple if condition by using comparison operators
'''a=3
b=5
if a<b:
    print("true")
if b>a:
    print("greater")'''
'''a=3
b=5
if a<=b:
    print("true")
if b>=a:
    print("greater")
if b!=a:
    print("not equal")
if a==b:
    print("equal")'''
'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("true")
if b>a:
    print("greater")
if a!=b:
    print("not equal")
if a==b:
    print("equal")'''
#multiple if condition by using logical operators
'''a=3
b=5
if a<b and b>a:
    print("true")
if b>=a or a==b:
    print("false")
if b==a not a!=b:
    print("not equal")'''
#multiple if condition by using membership operators
'''a=[10,30,40,60]
if 40 in a:
    print("true")
if 50 not in a:
    print("false")'''
#multiple if condition by using identity operators
'''a=59
if type(a) is int:
    print("true")
if type(a) is not int:
    print("not int")'''


#nested-if conition by using comparison operators
'''a=6
b=8
if a<b:
    print("true")
    if b>a:
        print("greater")
    elif a==b:
         print("not equal")
else:
    print("false")'''
'''a=6
b=8
if a>b:
    print("true")
    if b>a:
        print("greater")
    elif a==b:
         print("not equal")
else:
    print("false")'''
'''a=6
b=8
if a<=b:
    print("true")
    if b<=a:
        print("greater")
    elif a==b:
         print("not equal")
    else:
        print("equal")
else:
    print("false")'''
#nested-if condition by using logical operators
'''a=20
b=40
if a>b and b<a:
    print("true")
    if a>b or a==b:
        print("false")
    elif a!=b not a==b:
        print("not equal")
else:
    print("false")'''

#voting    
'''a=int(input("value"))
if a>=18:
    print("eligible for vote")
    if a<18:
        print("not eligible for vote")
else:
    print("not eligible")'''
#even or odd
'''a=int(input("enter the number"))
if a%2==0:
    print("it is even")
else:
    print("it is odd")'''
#leap year
'''a=int(input("year"))
if a%4==0:
    print("leap year")
else:
    print("non leap year")'''
'''a={"ID NO":"CGV1358","name":"kavya sri","College name":"ST Mary's Women's Engineering College","Mail id":"kavyasrikota989@gmail.com","Mobile no":8688944106,"percentage":68.0}
print("      STUDENT PROFILE     ")
print("ID NO:",a["ID NO"])
print("Student name:",a["name"])
print("College name:",a["College name"])
print("Mail id:",a["Mail id"])
print("Mobile no:",a["Mobile no"])
print("Percentage:",a["percentage"])'''

#guest
'''name="kavya"
a=str(input("enter your name"))
if a==name:
    print("welcome kavya")
else:
    print("welcome guest")'''
#vowels
'''a=str(input("letter"))
if a in "aeiou":
    print("it is vowel")
else:
    print("consonant")'''

'''a=["a","e","i","o","u"]
b=input("enter the vowel").lower()
if b in a:
    print("it is vowel")
else:
    print("it is consonant")'''
'''a=["kavya","harika","priya","pooja","tanya"]
name=input("enter the name").lower()
if name in a: 
    print("welcome",name)
else:
    print("welcome guest")'''

  #social media login    
'''a=str(input("enter the username"))
b=str(input("enter the password"))
if a=="kavya":
    if b=="123@k":
        print("login sucessful")
    else:
         print("incorrect password")
        
else:
    print("invalid credentials")'''

'''a=str(input("enter the username"))
b=str(input("enter the password"))
if a=="kavya" and b=="123@k":
        print("login sucessful")

else:
    print("invalid credentials")'''

 #bakery
'''a=str(input("enter the cake name"))
if a=="Red velvet":
    print("1200")
elif a=="Choco almond":
    print("1000")
elif a=="Butterscotch":
    print("800")
elif a=="Chocolate":
    print("600")
else:
    print("cake is not available")'''
 #pizza
'''pizza=int(input("enter the price"))
if pizza==800:
    print("crispy chicken pizza")
elif pizza==600:
    print("bbq pizza")
elif pizza==400:
    print("paneer pizza")
elif pizza==100:
    print("coke")'''

'''a=int(input("enter the age"))
b=int(input("enter the marks"))
c=int(input("enter the attendence"))
if a>=18:
    print("eligible for vote")
if b>=80:
    print("eligible for write exam")
if c>=90:
    print("eligible for scholorship")'''
 #student profile
'''id=int(input("enter the id"))
name=input("name")
college=int(input("enter the clg name"))
mailid=input("enter the mailid")
mobileno=int(input("enter the mobileno"))
branch=int(input("enter the branch"))
print("student profile..........")
print("student id is:",id)
print("student name is:",name)
print("student cld name is:",college)
print("student mobileno is:",mobileno)
print("student branch is:",branch)'''      
                  
              
  #loops
#for,while,range,break,continue,pass
#for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''
'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''
'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''
'''a=[10,20,30,40,50]
for i in a:
    print(a)'''
'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))'''
'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))'''
'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''
'''a=(10,20,30,40,50)
for i in a:
    print(i)
print(type(a))
print(type(i))'''
'''a={10,20,30,40,50}
for i in a:
    print(i)
print(type(a))
print(type(i))'''
'''a={"name":"kavya","year":2026,"month":7}
for i in a:
    print(i)
print(type(a))
print(type(i))'''
'''a={"name":"kavya","year":2026,"month":7}
for i in a:
    print(i)
    print(type(a))
    print(type(i))
for i in a.keys():
    print(i)
    print(type(i))
for i in a.values():
    print(i)
    print(type(i))
for i in a.items():
    print(i)
    print(type(i))'''
'''a=[3,6.9,"kavya",8+9j,True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''
'''a="codegnan"
for i in a:
    print(i,end=" ")
    print(type(a))
    print(type(i))'''
'''a="codegnan"
for i in a:
    print(i,end=" ")'''
'''fruits=["apple","grapes","mango"]
for i in fruits:
    print(i,end=" ")'''
'''a=["codegnan","python","course"]
b=str(a)
print(b.upper())'''
'''a=["codegnan","python","course"]
b=[]
for i in a:
    b.append(i.upper())
print(b)'''
  #while loop
'''a=10
while a>1:
    print(a)'''
'''a=10
while a>=1:
    print(a)
    a=a-1'''
'''a=10
while a>=1:
    a=a-1
    print(a)'''
'''a=20
while a>5:
    print(a)
    a=a-1'''
'''a=10
while a>1:
    a=a-1
print(a)'''
'''a=20
while a>6:
    print(a)
    a=a-1'''
'''a=6
while a<20:
    print(a)
    a+=1'''

'''while True:
    a=int(input("value"))
    if a>=18:
        print("eligible for vote")
        if a<18:
            print("not eligible for vote")
    else:
        print("not eligible")'''
'''while True:
    a=str(input("enter the cake name"))
    if a=="Red velvet":
        print("1200")
    elif a=="Choco almond":
        print("1000")
    elif a=="Butterscotch":
        print("800")
    elif a=="Chocolate":
        print("600")
    else:
        print("cake is not available")'''
  #range
#start-stop-step
'''for i in range(10):
    print(i)'''
'''for i in range(1,101):
    print(i)'''
'''for i in range(0,30,3):
    print(i)'''
'''for i in range(2,20,2):
    print(i)'''
'''for i in range(5,50,5):
    print(i)'''
#grade code
'''while True:
    marks=int(input("enter the marks"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(50,71):
        print("Grade-D")
    else:
        print("Fail,Study Well")'''

#break
#the break statement is used to terminate the loop.
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''
'''a=20
while a>5:
    a=a-1
    if a==10:
        break
print(a)'''
'''a=20
while a>5:
    a=a-1
    print(a)'''
'''a=20
while a>5:
    print(a)
    a=a-1
    if a==8:
        break'''
'''for i in range(20):
    if i==13:
        break
    print(i)'''
'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''
#continue
#the continue statement is used to skips the current iteration and rest of the code will be continue
'''a=30
while a>10:
    a=a-1
    if a==19:
        continue
    print(a)'''
'''a=40
while a>15:
    a=a-1
    if a==25:
        continue
    print(a)'''
'''a=30
while a>10:
    a=a-1
    if a==19:
        continue
print(a)'''
'''for i in range(25):
    if i==17:
        continue
    print(i)'''
'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''
#pass
#it does nothing but used for syntatically.
'''a=15
while a>10:
    print(a)
    a=a-1
    if a==14:
        pass'''
'''for i in range(20):
    if i==15:
        pass
    print(i)'''
#task
'''a=40
while a>10:
    a=a-1
    if a==30:
        continue
    if a==18:
        break
    print(a)'''

#attendace report
'''students=int(input("total no.of students"))
p=0
a=0
for i in range(1,students+1):
    b=input(f"student attendance {i}")
    if b=="p":
        p=p+1
    elif b=="a":
        a=a+1    
print("studence attendace report")
print("total:",students)
print("present:",p)
print("absent:",a)'''

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

#ATM application
'''while True:
    account=100000
    pwd=1234
    card=input("insert the card")
    if card=="c":
        print("welcome kavya")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input("choose the option 1.bal enq 2.withdraw"))
            if option==1:
                print("acc bal is",account)
            elif option==2:
                money=int(input("enter the money"))
                print(money)
                balance=account-money
                print("remaining bal is",balance)
            else:
                print("invalid option")
        else:
            print("incorrect password")
    else:
        print("invalid card")'''
                         
#pattern printing
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()'''

'''n=int(input())
for i in range(n):
    for j in range(i-1):
        print("*",end=' ')
    print()'''

'''a=int(input())
for i in range(a):
    print(a*"*")'''

'''a=int(input())
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("* "*i)'''

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

#keyword and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="kavya"
    mailid="kavya@gamil.com"
    print(id,name,mailid)
Details(id="id",name="kavya",mailid="kavya@gamil.com")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="kavya",mailid="kavya@gmail.com")
Details(id=30,name="harika",mailid="h@gmail.com")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(40,"nidhi","n@gmail.com")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details("nidhi","n@gmail.com",40)'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(mailid="k@gmail.com",name="kavya",id=20)'''

#swapping of two variables
'''a=10
b=20
a,b=b,a
print(a)
print(b)'''

'''def values(a,b):
    print(b,a)
values(10,20)'''

'''a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d" %(a,b))'''

#default arguments
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %f" %price)
Grocery("sugar",100)'''

'''def Grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %f" %price)
Grocery("dhal")'''

'''def Grocery(item="milk",price):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %f" %price)
Grocery(100)'''

#cake,price,quantity
'''def Bakery(item,price,quantity):
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("quantity is %d" %quantity)
Bakery("red velvet",1200,1)'''

'''def Bakery(item,price,quantity):
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("quantity is %d" %quantity)
Bakery("red velvet",1200,1)
Bakery("chocolate",1000,2)'''

'''def Bakery(item,price=1200,quantity=1):
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("quantity is %d" %quantity)
Bakery("red velvet")'''

'''def Bakery(item="red velvet",price,quantity):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("quantity is %d" %quantity)
Bakery(1200,1)'''

#args
# *arguements:- *is used to unpack the elemets
'''a=[2,3,4,5,6,7]
print(a)
print(type(a))
print(*a)'''

'''a=(2,3,4,5,6,7)
print(a)
print(type(a))
print(*a)'''

'''a={2,3,4,5,6,7}
print(a)
print(type(a))
print(*a)'''

'''a={"name":"rupa","year":2026,"month":6}
print(a)
print(type(a))
print(*a)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,10#value error
print(a)
print(b)
print(c)'''

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,b,c="codegnan"#error
print(a)
print(b)
print(c)'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,b,c="codegnan","python","course"
print(a)
print(b)
print(c)'''

'''*a,*b,*c=2,3,4,5,6,7,8,9,10#error
print(*a)
print(*b)
print(*c)'''

'''*a,*b,c=2,3,4,5,6,7,8,9,10#error
print(*a)
print(*b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(*c)'''

'''a,b,c="python","java","c","c++","mongodb","django","flask"#value error
print(a)
print(b)
print(c)'''

'''a,*b,c="python","java","c","c++","mongodb","django","flask"
print(a)
print(*b)
print(c)'''

#variable length arguements:-Variable length arguements are automatically stoes in tuple and we use *arguements
#*=tuple
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[3,5,6,7]
check(*b)
c=(7,8,9)
check(*c)
d={3,5,6,9}
check(*d)
e={"name":"rupa","year":2026,"month":"june"}
check(*e)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(3,4.5,2.3,6.2)
check1(2,3,4,5,2.3,4.5,"rupa")'''#eror

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()    
check1(2,3,4,5,6)
check1(3,4.5,2.3,6.2)
check1(2,3,4,5,2.3,4.5,"rupa",4+9j,True,False)'''

#Railway ticket booking
'''while True:          #1.
    def railway_ticket():
        ticket=1000
        gender=input("Enter you gender: ")
        age=int(input("Enter your age: "))
        if gender=="male":
            if age>=60:
                print("Senior citizens")
                ticket=ticket-30/100*ticket
                print(f"your bill is {ticket}")
            elif age<60:
                print("Normal citizens")
                print(f"your bill is {ticket}")
        elif gender=="female":
            if age>=60:
                print("Senior citizens")
                ticket=ticket-50/100*ticket
                print(f"your bill is {ticket}")
            elif age<60:
                print("Normal citizens")
                ticket=ticket-30/100*ticket
                print(f"your bill is {ticket}")
    railway_ticket()'''


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

#max(),min(),sum()
'''print(max(3,6,8,9,10,40,26))

print(min(0,1,59,3,6,2))

a=1,2,3,4,5,6,7,8,9,10
print(sum(a))'''

#marks analysis report     
'''students=int(input("no.of students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter the student {i} marks"))
    b=marks.append(mark)
for i in marks:
    print(i)
print("Marks Analysis Report.......")    
print("total students",students)
print("heighest marks",max(marks))
print("lowest marks",min(marks))
print("total marks",sum(marks))
print("average",sum(marks)/students)'''


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

#yield vs return
'''def mygen():
    return "python","java","c"
print(*mygen())'''


'''def mygen():
    yield "vja"
    yield "hyd"
    yield "vzg"
print(*mygen())
#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))'''


#print(dir())
#print(dir("_builtins_"))
#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))

b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"pooja")
print(c)

c["g"]="python"
print(c)'''

#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multiple collections into one collection
'''a=[10,20,30,40,50]
names=["surendar","harsha","rupesh","krishna","mohan"]
print(a+names)
b=zip(a,names)
print(b)
c=list(zip(a,names))
print(c)
c=tuple(zip(a,names))
print(c)
c=set(zip(a,names))
print(c)
c=dict(zip(a,names))
print(c)'''

#enumarate()->we can give counter to the collection
'''names=["madhu","nirupam","deekshith","guruprasad","surendar"]
for i in range(len(names)):
    print(i)'''
#enumerate method
'''b=list(enumerate(names))
print(b)
b=list(enumerate(names,100))
print(b)
b=tuple(enumerate(names))
print(b)
b=set(enumerate(names))
print(b)
b=dict(enumerate(names))
print(b)'''

#task
#BMI
'''while True:
    weight=float(input("enter the weight"))
    height=float(input("enter the height"))
    BMI=weight/height**2
    if BMI<=18.5:
        print("underweight")
    elif BMI>18.5 and BMI<=24.5:
        print("normal weight")
    elif BMI>24.5 and BMI<=29.5:
        print("over weight")
    elif BMI>30:
        print("obesity")'''

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

#ASCII
#chr
'''print(chr(56))
print(chr(90))
print(chr(65))
print(chr(91))'''

#ord
'''print(ord("a"))
print(ord("z"))'''

#task
'''for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")'''

'''name="kavya"
for i in name:
    print(i,ord(i))'''

#Differences between modules,libraries and packages
#MODULES
#a module in python is a single python file it consists python code.
#it typically consists of functins,classes and attributes and variables that can be used in other python scripts or programs.
#examples of modules include math.py,random.py or my module.py.
#PACKAGES
#a package in python is a directory containing one or more python modlues and an __init__.py file.
#The __init__.py file can be empty or contain initialization code for the package.
#examples of packages include numpy,pandas or django.
#LIBRARY
#libraries can consists of multiple modules and packages,organized to serve a particular purpose or domain.
#examples such as requests,numpy,pandas, and matplotlib.
#Note->every pyhton file is a module and import is a keyword and every python file is saved internally with variable name as __main__ .
   
    
