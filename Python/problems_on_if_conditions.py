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
