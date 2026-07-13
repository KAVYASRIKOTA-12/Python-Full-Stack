#OOPs syntax
'''class classname():
    name="kavya"
    age=22
    place="vja"
    def fname(method_name):#give method name
        print("statements")#give statements
obj=classname()
print(dir(obj))
obj.fname()'''

#Class declaration
'''class Details():
    name="kavya"
    age=22
    place="vja"
    def display(self):#without method name we cant print statements
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#Object instantiation
#here we can give information to different users.
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("harika",21,"vja")
a.display()
b=Details()
b.data("jhansi",30,"gnt")
b.display()'''

#Object initialization
'''class Details():
    def __init__(self,name,age,place):#creating a constructor
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("kavya",22,"vja")
print(dir(a))
a.display()'''

#taking values in runtime
#method 1
'''class Details():
    def __init__(self,name,age,place):
       self.name=name
       self.age=age
       self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input("name"),int(input("age")),input("place"))
print(dir(a))
a.display()'''

#method 2
'''class Details():
    def __init__(self):
       self.name=input("name")
       self.age=int(input("age"))
       self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#Difference between _ and __
'''we generally use it for private variables,
that means whenever we use double reading _ for a variable our python interpreter treats it as a special variable in order to avoid name conflicts with methods in inner classes.'''
'''class Employee():
    def __init__(self):
        self.name="kavya"
        self._mailid="kavya@gmail.com"
        self.__salary=10000
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._Employee__salary)'''

#in runtime
'''class Employee():
    def __init__(self):
        self.name=input("name")
        self._mailid=input("mailid")
        self.__salary=int(input("salary"))
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._Employee__salary)
b=Employee()
print(b.name)
print(b._mailid)
print(b._Employee__salary)'''

#for different user
'''class Employee1():
    def __init__(self):
        self.name="kavya"
        self._mailid="kavya@gmail.com"
        self.__salary=10000
class Employee2():
    def __init__(self):
        self.name="kiara"
        self._mailid="kiara@gmail.com"
        self.__salary=20000
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._Employee1__salary)
b=Employee2()
print(b.name)
print(b._mailid)
print(b._Employee2__salary)'''


#POLYMORPHISM
#Operator overloading
'''a=4;b=8
print(a+b)
print(a.__add__(b))
print(a.__add__(10))
print((9).__add__(b))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2))#error
print(a.__eq__(4))
print(a.__pow__(2))
print(a.__le__(10))
print(a.__ge__(3))
a=[1,2,3,4,5,6,7,8];b=[5,6,7,8,9,10,11,12]
print(a.__add__(b))
print(a.__getitem__(4))
print(b.__getitem__(6))
a="python";b="course"
print(a.__add__(b))
print("code".__add__("gnan"))
a="kavya";b="kota"
print(a.__add__(" "+b).title())'''

#Operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(4)#when we give class name it will go to the class.
y=B(5)
#x=4  #if we doesn't mention class name it doesn't go to the class.
#y=5
print(x+y)'''

#Method overloading
'''class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends")
x=New()
x.sum()
x.sum(4,2,6)
x.sum(4,9)'''

#Task
'''class New():
    def sum(self,a=4,b=6,c=8):
        if a!=4 and b!=4 and c==8:
            print("the sum is",a+b+c)
        elif a==7 and b!=9:
            print("the product is",a*b)
        else:
            print("program ends")
x=New()
x.sum()'''

#Method overriding
'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

#Task
'''class Car():
    def vehical(self):
        print("supra")
class Bike():
    def vehical(self):
        print("KTM")
a=Car()
b=Bike()
a.vehical()
b.vehical()'''


#INHERITANCE
#single inheritance
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#Task
#multiple inheritance
'''class Father():#parent-1
    height="5inch"
    def height1(cls):
        print("father height is",cls.height)
class Mother():#parent-2
    weight="55kg"
    def weight1(cls):
        print("mother weight is",cls.weight)
class Kid(Father,Mother):#child
    Dob="25/05/2005"
    def Dob1(cls):
        print("kid Dob is",cls.Dob)
a=Kid()
a.height1()
a.weight1()
a.Dob1()'''

#Task
#multi level inheritance
'''class GrandFather():#grandparent
    def land(self):
        print("grandfather gives land")
class Father(GrandFather):#parent
    def house(self):
        print("father gives house")
class Child(Father):#kid
    def car(self):
        print("child gives car")
a=Child()
a.land()
a.house()
a.car()'''

#Task
#hierarchical inheritance
'''hierarchical inheritance is where one parent class is inherited by multiple child classes.'''
'''class Employee():#parent
    def company_name(self):
        print("Google")
class Trainer(Employee):#child1
    def teaching(self):
        print("Teaches the class")
class Developer(Employee):#child2
    def Develop(self):
        print("Devolop the code")
a=Trainer()
a.teaching()
a.company_name()
b=Developer()
b.Develop()
b.company_name()'''

#Task
#hybrid inheritance
'''hybrid inheritance means combining more than one typr of inheritance for ex:hierarchical inheritance+multiple inheritance.'''
'''class person():
    def Details(self):
        print("kavya")
class student(person):
    def study(self):
        print("student is studying")
class teacher(person):
    def teach(self):
        print("teaches the class")        
class teaching_assistant(student,teacher):
    def assistant(self):
        print("clarify the doubts")
a=teaching_assistant()
a.Details()
a.study()
a.teach()
a.assistant()'''

#super built-in function(sup())
'''class parent():#parent
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):#child
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
a=child("kavya",22)
print(a.name)
print(a.age)'''


#encapsulation
'''combine multiple units into single unit is known it as a encapsulation,
in encapsulation we have three types:protected,private,public.'''
#public
'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()'''

#_private
'''class parent():
    _privatedata=10
    def method1(self):
        print(self._privatedata)
class child(parent):
    def method2(self):
        print(self._privatedata)
obj1=child()
obj1.method1()
obj1.method2()'''

#__protected
'''class parent():
    __protecteddata="kavya"
    def method1(self):
        print(self.__protecteddata)
class child(parent):
    def method2(self):
        print(self._parent__protecteddata)
obj1=child()
obj1.method1()
obj1.method2()'''

#abstraction
'''hiding unnecessary information from user is called abstraction.
abstract class:if a class contain one or more than one abstract method then the class is called abstract class.
abstract method:if the method is declared without implementation is called abstract method.'''
#ex 1
'''class parent():
    def method1(self):
        pass
a=parent()
a.method1()'''

#ex 2
'''class parent():
    def method1(self):
        print("data")
a=parent()
a.method1()'''

#ex 3
'''from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("python course")
obj=A()
obj.method1()'''

#ex 4
'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("python course")
obj=A()
obj.method1()'''#error

#ex 5
'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj=B()
obj.method1()
obj.method2()
obj.method3()'''

    




       





              
              




