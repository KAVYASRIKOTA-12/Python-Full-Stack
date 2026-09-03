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
