import csv

sms_database='Student1.csv'
# f=open(sms_database,"w")
# writer=csv.writer(f)
# writer.writerow(['Name','Roll_no','Age','Gender','Contact_no'])
rec_fields=["Name","Age","Gender","Contact_no"]
student_records=[]
def menu():
    print("----------Student Management system-------------")
    print("Following are the options selesct from these\nSelect: \n1-Create member\n2-for view Members\n3-for Search member\n4-for update member\n5-for delete member\n6-for exit" )

def create_member():
    global sms_database
    Name=input("Enter your Name: \n")
    Roll_no=input("Enter Your Roll_no: \n")
    Age=input("Enetr your age: \n")
    Gender=input("Enetr your Gender: \n")
    Contact_no=input("Enter your phone no")
    Studentlist=[Name,Roll_no,Age,Gender,Contact_no]
    student_records.append(Studentlist)
    with open(sms_database,"a",newline="") as f:
        writer=csv.writer(f)
        # print("[Name,Roll_no,Age,Gender,Contact_No]")
        writer.writerows(student_records)
    print("--------------------Information Saved Succesfully--------------------")
    key=input("Press any key to continue")

def view_member():
    global sms_database
    with open(sms_database,'r',newline="") as f:
        reader=csv.reader(f)
        for row in reader:
            print(row)    
    input("Press any key to continue")

def search_member():
    global sms_database
    with open(sms_database,"r",newline="") as f:
        reader=csv.reader(f)
        roll_no=input("Enter your roll no")
        for records in reader:
            # for record in records:
            if roll_no==records[1]:
                print("-------Student Found succesfully--------")
                print("Name :",records[0])
                print("Roll_no :",records[1])
                print("Age :",records[2])
                print("Gender :",records[3])
                print("Contact_no:",records[4])
            else:
                print("----Student Not Found--------")
    input("Press any key to continue")

def update_member():
    global sms_database
    updated_list=[]
    Found=False
    with open(sms_database,"r",newline="") as f:
        reader=csv.reader(f)
        roll_no=input("Enter Roll no of student you want to update")
        for records in reader:
            if roll_no==records[1]:
                Found=True
                updated_Contact_no=input("Enter students updated contact no")
                records[4]=updated_Contact_no
            updated_list.append(records)
    if Found==False:
        print("Student not found")
    else:
        with open(sms_database,'w+',newline='') as f:
            writer=csv.writer(f)
            writer.writerows(updated_list)
            print("--------updates succesfully---------")
    input("Press any key to continue")  

def delete_member():
    global sms_database
    updated_list=[]
    Found=False
    with open(sms_database,"r",newline="") as f:
        reader=csv.reader(f)
        Droll_no=input("Enter Roll no of student you want to delete")
        for records in reader:
            if Droll_no==records[1]:
                Found=True
            else:
                updated_list.append(records)
    if Found==False:
        print("Student not found")
    else:
        with open(sms_database,'w+',newline='') as f:
            writer=csv.writer(f)
            writer.writerows(updated_list)
            print("--------Deleted succesfully---------")
    input("Press any key to continue")  









while True:
    menu()
    Choice=input("Enter your choice from these")
    if Choice=='1':
        create_member()
    elif Choice=='2':
        view_member()
    elif Choice=='3':
        search_member()
    elif Choice=='4':
        update_member()
    elif Choice=='5':
        delete_member()
    elif Choice=='6':
        break
