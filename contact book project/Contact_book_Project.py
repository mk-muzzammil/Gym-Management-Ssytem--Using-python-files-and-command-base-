contact_Book=[]


def menu():
    print("1-for create member\n2-for view member\n3-for search member\n4-for delete contcat\n5-for update contact\n6 for exit")


def create_contact():
    print("*********Creating Contact*********")
    name=input("Enter your name")
    CNIC_No=input("Enter your CNIC")
    Phone_No=input("Enter your phone No")
    member_info=[name,CNIC_No,Phone_No]
    contact_Book.append(member_info)
    print("contact information saved succesfully")

def view_contact():
    print("***********View Contact************")
    for contact in contact_Book:
        print("Name",contact[0])
        print("CNIC_No",contact[1])
        print("Phone_No",contact[2])


def search_contact():
    print("***************Searching contact*************")
    for contact in contact_Book:
        Cnic=input("Enter your Cnic to get your contact info")
        if Cnic==contact[1]:
            print("Name",contact[0])
            print("CNIC_No",contact[1])
            print("Phone_No",contact[2])
        elif Cnic!=contact[1]:
            print("Wrong CNIC NO")

def delete_contact():
    print("*********Deleting Member***********")
    cnic=input("Enter your Cnic")
    for contact in contact_Book:
        if cnic==contact[1]:
            contact_Book.remove(contact)
            print("Your contact deleted succesfully")
            print(contact_Book)

        elif cnic!=contact[1]:
            print("You have entered incorect CNIC")
def update_contact():
    cnic=input("Enter your CNIC_No")
    for contact in contact_Book:
        if cnic==contact[1]:
            print("*****Contact Found Succesfully*******")
            contact[2]=input("Enter Phone_no u want to change")
            print("---------------Updated succesfully---------------")
            print(contact_Book)
        
        elif cnic!=contact[1]:
            print("you have entered incorrect CNIC")












while True:
    menu()
    options=int(input("Enter your choice in these"))
    if options==1:
        create_contact()
    elif(options==2):
        view_contact()
    elif options==3:
        search_contact()
    elif options==4:
        delete_contact()
    elif options==5:
        update_contact()
    elif options==6:
        break


        