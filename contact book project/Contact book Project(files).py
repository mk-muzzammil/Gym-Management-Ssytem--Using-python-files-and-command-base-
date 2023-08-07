import csv
my_database='contactbook1.csv'

contact_Book=[]
def firstrow():
    with open(my_database,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow('Name;CNIC;Phone_no')


def menu():
    print("0-for enter firstrow\n1-for create member\n2-for view member\n3-for search member\n4-for delete contcat\n5-for update contact\n6 for exit")


def create_contact():
    print("*********Creating Contact*********")
    global contact_Book
    global my_database
    name=input("Enter your name")
    CNIC_No=input("Enter your CNIC")
    Phone_No=input("Enter your phone No")
    member_info=[name,CNIC_No,Phone_No]
    contact_Book.append(member_info)
    with open(my_database,"a",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(contact_Book)
    print("contact information saved succesfully")

def view_contact():
    print("***********View Contact************")
    global my_database
    with open(my_database,"r",newline="") as f:
        reader=csv.reader(f)

        for rows in reader:
            print(rows)


def search_contact():
    print("***************Searching contact*************")
    global my_database
    with open(my_database,"r",newline='') as f:
        reader=csv.reader(f)
        CNIC=input("Enter your CNIC")
        for rows in reader:
            if rows[1]==CNIC:
                print("--------Member found succesfully--------")
                print("Name: ",rows[0])
                print("CNIC_No: ",rows[1])
                print("Phone_No: ",rows[2])
            # elif rows[1]!=CNIC:
            #     print("No contact with this CNIC")

def delete_contact():
    print("*********Deleting Member***********")
    global my_database
    Found=False
    updatedlist=[]
    with open(my_database,"r",newline="") as f:
        reader=csv.reader(f)
        cnic=input("Enter your Cnic")
        for row in reader:
                if cnic==row[1]:
                    Found=True
                    print("---------deleted succesfully--------")
                else:
                    updatedlist.append(row)
        if Found==False:
            print("memebr not found")
        else:
            with open(my_database,"w+",newline='') as f:
                writer=csv.writer(f)
                writer.writerows(updatedlist)

                
def update_contact():
    global my_database
    Found=False
    updatedlist=[]
    with open(my_database,"r",newline="") as f:
        reader=csv.reader(f)
        cnic=input("Enter your Cnic")
        for row in reader:
                if cnic==row[1]:
                    Found=True
                    row[2]=input("Enter contact updated phone_no")
                    updatedlist.append(row)
        if Found==False:
            print("you have entered incorrect CNIC")
        else:
            with open(my_database,"w+",newline='') as f:
                writer=csv.writer(f)
                writer.writerows(updatedlist)

    print("---------------Updated succesfully---------------")












while True:
    menu()
    options=int(input("Enter your choice in these"))
    if options==0:
        firstrow()
    elif options==1:
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