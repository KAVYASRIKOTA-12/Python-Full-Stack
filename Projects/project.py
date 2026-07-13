class Contact:
    mang = []

    def __init__(self):
        print("\nEnter Contact Details")
        self.name = input("Enter Name : ")
        self.phone = input("Enter Phone : ")
        self.email = input("Enter Email : ")
        Contact.mang.append(self)

    def display(self):
        print(f"Name : {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print("-" * 30)

    def update(self):
        field = input("Update (name/phone/email): ").lower()

        if field == "name":
            self.name = input("Enter New Name : ")

        elif field == "phone":
            self.phone = input("Enter New Phone : ")

        elif field == "email":
            self.email = input("Enter New Email : ")

        else:
            print("Invalid Choice")

        print("Contact Updated Successfully.")

    @classmethod
    def update_contact(cls):
        if len(cls.mang) == 0:
            print("No Contacts Available.")
            return

        name = input("Enter Contact Name to Update: ")

        for contact in cls.mang:
            if contact.name.lower() == name.lower():
                contact.update()
                return

        print("Contact Not Found.")

    @classmethod
    def delete_contact(cls):
        if len(cls.mang) == 0:
            print("No Contacts Available.")
            return

        name = input("Enter Contact Name to Delete: ")

        for contact in cls.mang:
            if contact.name.lower() == name.lower():
                cls.mang.remove(contact)
                print("Contact Deleted Successfully.")
                return

        print("Contact Not Found.")

    @classmethod
    def display_all(cls):
        if len(cls.mang) == 0:
            print("No Contacts Available.")
            return

        print("\n------ Contact List ------")
        for i, contact in enumerate(cls.mang, 1):
            print(f"\nContact {i}")
            contact.display()


while True:

    print("\n====== CONTACT BASE MANAGEMENT SYSTEM ======")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. List Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        Contact()

    elif choice == "2":
        Contact.update_contact()

    elif choice == "3":
        Contact.display_all()

    elif choice == "4":
        Contact.delete_contact()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
