#modules
'''def greet(name):
    print("Welcome",name)'''


'''a=int(input("a value"))
b=int(input("b value"))
print("The sum is",a+b)'''

'''details={"Idno":[10,20,30],
         "Names":["kavya","harika","jhansi"],
         "Marks":[90,80,70]}'''



'''if __name__=="__main__":
    a=[10,20,30,40,50]
    a.extend("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''       


#task
#dice code
'''import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll again?(y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invalid option")'''



#file handling
#methods->write(),append(),readlines(),writelines()
#write()
#ex 1
'''a=open("kavya.txt","w")
a.write("codegnan")
a.close()'''

#ex 2
'''a=open("kavya.txt","w")
a.write("data")  #it will override the previous data.
a.close()'''

#append()
'''a=open("kavya.txt","a")
a.write("\tcourse") #add data to previous data.
a.close()'''

#ex 1(in runtime)
'''a=open("kavya.txt","w")
a.write(input("data"))
a.close()'''

#ex 2(in runtime)
'''a=open("kavya.txt","w")
b=input("data")
a.write(b)
a.close()'''

#readlines()
#it will display entire content
'''a=open("kavya.txt")
print(a.read())'''

#it will display first line
'''a=open("kavya.txt")
print(a.readline())'''

#it will display with \n
'''a=open("kavya.txt")
print(a.readlines())'''

#it will display no.of characters
'''a=open("kavya.txt")
print(a.read(6))'''


#writelines()->it makes every obj side by side
'''a=open("harika.txt","w")
b=["saanvi","monali","kavya","bhanu","rekha"]
a.writelines(b)
a.close()'''

#it will display in newline
'''a=open("harika.txt","w")
b=["saanvi","monali","kavya","bhanu","rekha"]
a.writelines("\n".join(b))
a.close()'''

#accessing files
#with path
'''a=open("C:\\Users\\Kavya\\OneDrive\\Desktop\\PFS\\sets methods.py")
print(a.read())'''

#without path
'''a=open("indexing.py")
print(a.read())'''

#to change file directory
'''import os
print(os.path)
print(os.getcwd())
print(os.chdir(r"C:\\Users\\Kavya\\Downloads"))
print(os.listdir())
b=open("file name")
b.close()'''




