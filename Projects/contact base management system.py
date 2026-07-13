class AddContact:
    def __init__(self):
        self.contacts = []

    def add(self):
        while True:
            name = input("Enter Name: ").strip()
            if not name.isalpha():
                print(" Name should contain only alphabets.")
                continue
            if any(c["Name"].lower()==name.lower() for c in self.contacts):
                print(" Name already exists! Enter another name.")
                continue
            break

        while True:
            mobile=input("Enter Mobile Number: ")
            if len(mobile)!=10 or not mobile.isdigit() or mobile[0] not in "9876":
                print(" Invalid Mobile Number!")
                continue
            if any(c["Mobile"]==mobile for c in self.contacts):
                print(" Mobile Number already exists! Enter another number.")
                continue
            break

        while True:
            email=input("Enter Gmail ID: ")
            if email.endswith("@gmail.com") and email.count("@")==1:
                break
            print(" Invalid Gmail ID!")

        self.contacts.append({"Name":name,"Mobile":mobile,"Email":email})
        print("\n Contact Added Successfully.\n")

class ListContact(AddContact):
    def display(self):
        if not self.contacts:
            print("\nNo Contacts Available.\n"); return
        print("\n========== CONTACT LIST ==========")
        for i,c in enumerate(self.contacts,1):
            print(f"\nContact {i}")
            print("Name   :",c["Name"])
            print("Mobile :",c["Mobile"])
            print("Email  :",c["Email"])
        print("\n==================================")

class UpdateContact(ListContact):
    def update(self):
        if not self.contacts:
            print("No Contacts Available."); return
        name=input("Enter Name of Contact to Update: ")
        for contact in self.contacts:
            if contact["Name"].lower()==name.lower():
                print("\n1. Update Name\n2. Update Mobile\n3. Update Email")
                try: ch=int(input("Enter Choice: "))
                except: print("Invalid Choice."); return
                if ch==1:
                    while True:
                        new=input("Enter New Name: ").strip()
                        if not new.isalpha():
                            print("Invalid Name!"); continue
                        if any(c!=contact and c["Name"].lower()==new.lower() for c in self.contacts):
                            print("Name already exists!"); continue
                        contact["Name"]=new; break
                elif ch==2:
                    while True:
                        new=input("Enter New Mobile Number: ")
                        if len(new)!=10 or not new.isdigit() or new[0] not in "9876":
                            print("Invalid Mobile Number!"); continue
                        if any(c!=contact and c["Mobile"]==new for c in self.contacts):
                            print("Mobile Number already exists!"); continue
                        contact["Mobile"]=new; break
                elif ch==3:
                    while True:
                        new=input("Enter New Gmail ID: ")
                        if not(new.endswith("@gmail.com") and new.count("@")==1):
                            print("Invalid Gmail ID!"); continue
                        contact["Email"]=new
                        break
                else:
                    print("Invalid Choice."); return
                print("\n Contact Updated Successfully.\n"); return
        print("Contact Not Found.")

class DeleteContact(UpdateContact):
    def delete(self):
        if not self.contacts:
            print("No Contacts Available."); return
        name=input("Enter Name to Delete: ")
        for c in self.contacts:
            if c["Name"].lower()==name.lower():
                self.contacts.remove(c)
                print("\n Contact Deleted Successfully.\n"); return
        print("Contact Not Found.")

obj=DeleteContact()
while True:
    print("\n========== CONTACT MANAGEMENT SYSTEM ==========")
    print("1. Add Contact\n2. List of Contacts\n3. Update Contact\n4. Delete Contact\n5. Exit")
    try:
        ch=int(input("Enter Choice: "))
        if ch==1: obj.add()
        elif ch==2: obj.display()
        elif ch==3: obj.update()
        elif ch==4: obj.delete()
        elif ch==5:
            print("Thank You!"); break
        else: print("Invalid Choice.")
    except ValueError:
        print("Please enter a valid number.")
