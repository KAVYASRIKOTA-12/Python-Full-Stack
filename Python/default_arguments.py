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
