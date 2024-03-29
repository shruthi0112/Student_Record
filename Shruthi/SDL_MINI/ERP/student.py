import pickle
import os
from random import randint
def  head(data):
    print
    print ("="*167)
    print
    string = "# |"+" "*8+data+" "*8+"| #"
    print (string.center(167, "-"))
    print
    print ("="*167)
    print
def menu(data):
    print
    ml = []
    for i in data:
        ml.append(len(i))
    max_len = max(ml)
    for i in data:
        s = i+" "*(max_len - len(i))
        print (s.center(167))
    print
def output(data):
    print
    string = ">"+" "*5+data+" "*5+"<"
    print (string.center(167, "-"))
    print
def maxlenl(l):
    g = []
    for i in l:
        sp = i.split(":")
        g.append(len(sp[0]))
    return max(g)
def maxlenr(l):
    g = []
    for i in l:
        sp = i.split(":")
        g.append(len(sp[-1]))
    return max(g)
def display(l):
    for i in l:
        s = i.split(":")
        st = s[0]+" "*(maxlenl(l)-len(s[0]))+"    :    "+s[-1]+" "*(maxlenr(l)-len(s[-1]))
        print (st.center(167))

class students(object):
    """A class for student's record"""

    def __init__(self):                 #Initialising instance attributes
        self.Reg_No = 1
        self.Roll_No = None
        self.Name = None
        self.Father_Name = None
        self.Mother_Name = None
        self.Sex = None
        self.DOB = None
        self.Age = None
        self.Address = None
        self.Mobile_No = None
        self.Email = None
        self.Class = None
        self.Section = None
        self.Stream = None
        self.Fees = None
        #self.MOC = None
        self.Fees_Months = 0
        self.Weight = None
        self.Height = None
        self.B_Group = None
        self.Aadhaar = None

    def GET_FEES_MONTH(self):
        
        f_read = open("students.tc", "rb")
        try:
            while True:
                s = pickle.load(f_read)
                self.Fees_Months = s.Fees_Months + 1
        except EOFError:
                        print

    def ASSIGN_REG_NO(self):
        try:
            f_read = open("students.tc", "rb")
            try:
                while True:
                    s = pickle.load(f_read)
                    self.Reg_No = s.Reg_No + 1
            except EOFError:
                print
        except IOError:
            self.Reg_No = 1

    def ASSIGN_FEES(self):                  #Assigning Fees
        if self.Class == 1:
            self.Fees = 97620
        elif self.Class ==2:
            self.Fees = 94700
        elif self.Class ==3:
            self.Fees = 96100
        elif self.Class ==4:
            self.Fees = 96700
        

    def GET_DATA(self, *modify):     #Requesting data from user
        if modify == ():
            self.ASSIGN_REG_NO()
            head("Registration Number - {0}".format(self.Reg_No))
        else:
            self.Reg_No = input("Enter New Registration Number ---> ")
        self.Roll_No = input("Enter Roll Number ---> ")
        self.Name = input("Enter Student's Name ---> ")
        self.Father_Name = input("Enter Father's Name ---> ")
        self.Mother_Name = input("Enter Mother's Name ---> ")
        self.Sex = input("Enter Sex [M/F] ---> ")
        self.DOB = input("Enter Date of Birth [DDMMYYYY] ---> ")
        self.Age = input("Enter Age ---> ")
        self.Address = input("Enter your address ---> ")
        self.Mobile_No = input("Enter Mobile Number ---> ")
        self.Email = input("Enter E-mail ---> ")
        self.Class = input("Enter Year(1,2,3,4) ---> ")
        self.Stream = input("Enter your caste [OPEN/OBC/SC/ST/SBC] ---> ")
        self.Section = input("Enter Section(A/B/C) ---> ")
        #self.MOC = input("Enter Mode of Convenience [BUS, AUTO, SELF] ---> ")
        self.ASSIGN_FEES()
        self.Weight = input("Enter your Weight [KG] ---> ")
        self.Height = input("Enter your Height [CM] ---> ")
        self.B_Group = input("Enter your Blood Group ---> ")
        self.Aadhaar = input("Enter Aadhaar number ---> ")

    def PRINT_DATA(self):                   #Displaying data to user

        head("Registration Number - {0}".format(self.Reg_No))
        l1 = "Roll Number : "+str(self.Roll_No)
        l2 = "Name : "+self.Name
        l3 = "Father's Name : "+self.Father_Name
        l4 = "Mother's Name : "+self.Mother_Name
        l5 = "Sex : "+self.Sex
        l6 = "Date of Birth : "+str(self.DOB)
        l7 = "Age : "+self.Age
        l8 = "Address : "+self.Address
        l9 = "Mobile Number : "+str(self.Mobile_No)
        l10 = "E-mail : "+self.Email
        l11 = "Class : "+str(self.Class)
        l12 = "Section : "+self.Section
        #l14 = "Mode of  Convenience : "+self.MOC
        l15 = "Fees applicable : "+str(self.Fees)
        l16 = "Fees paid of months : "+str(self.Fees_Months)
        l17 = "Weight : "+str(self.Weight)
        l18 = "Height : "+str(self.Height)
        l19= "Blood Group : "+self.B_Group
        l20= "Aadhaar number : "+str(self.Aadhaar)
        display([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l16, l17, l18, l19, l20])

    def PAY_FEES(self):

        Fees_Months = input("Enter no. of months to pay fees ---> ")
        output("Amount to be paid : "+str(self.Fees*Fees_Months))
        c_no = randint(1000,9999)
        ch = input("Enter '{0}' to confirm and fdinally pay fees ---> ".format(c_no))
        if ch == c_no :
            self.Fees_Months += Fees_Months
            output("Fees deposited successfully of registration number : "+str(self.Reg_No))
        else :
            output("Fees Not Deposited")


def post_data():
    
    st = students()                 #Creating object of the main class
    st.GET_DATA()
    f_append = open("students.tc", "ab")
    pickle.dump(st, f_append)
    output(st.Name+" Registered succesfully")
    f_append.close()

    
def show_data():

    try:
        f_read = open("students.tc", "rb")
        while True:
            st = pickle.load(f_read)
            st.PRINT_DATA()
    except EOFError:
        output("No more records found")

    except IOError:
        output("School management system not started yet. Please register atleast one student to get started")



def search():

    def search_reg_no(reg_no):
        
        f_read = open("students.tc", "rb")
        Flag = False
        try:
            while True:
                st = pickle.load(f_read)
                if st.Reg_No == reg_no :
                    Flag = True
                    st.PRINT_DATA()
        except EOFError:
            if not Flag :
                output("Record not found")
        if Flag:
            return st.Reg_No

    def search_name(name):
        
        f_read = open("students.tc", "rb")
        Flag = False
        try:
            while True:
                st = pickle.load(f_read)
                if st.Name.lower() == name.lower() :
                    Flag = True
                    st.PRINT_DATA()
        except EOFError:
            if not Flag :
                output("Record not found")

    def search_roll_no(roll_no):

        f_read = open("students.tc", "rb")
        Flag = False
        try:
            while True:
                st = pickle.load(f_read)
                if st.Roll_No == roll_no :
                    Flag = True
                    st.PRINT_DATA()
        except EOFError:
            if not Flag :
                output("Record not found")
    def search_mobile_no(mobile_no):

        f_read = open("students.tc", "rb")
        Flag = False
        try:
            while True:
                st = pickle.load(f_read)
                if st.Mobile_No == mobile_no :
                    Flag = True
                    st.PRINT_DATA()
        except EOFError:
            if not Flag :
                output("Record not found")

    def search_aadhaar(aadhaar):

        f_read = open("students.tc", "rb")
        Flag = False
        try:
            while True:
                st = pickle.load(f_read)
                if st.Aadhaar == aadhaar :
                    Flag = True
                    st.PRINT_DATA()
        except EOFError:
            if not Flag :
                output("Record not found")

    def Email(email):

        f_read = open("students.tc", "rb")
        Flag = False
        try:
            while True:
                st = pickle.load(f_read)
                if st.Email.lower() == email.lower() :
                    Flag = True
                    st.PRINT_DATA()
        except EOFError:
            if not Flag :
                output("Record not found")

    while True:
        head("Search Menu")
        menu(["1. Search by Registration Number", "2. Search by Name", "3. Search by Roll Number", "4. Search by Mobile Number", "5. Search by Aadhaar Number", "6. Search by Email", "7. Exit search menu"])
        usr_ch = input("Enter your choice [Search Menu] ---> ")
        if usr_ch == '1' :
            reg_no = input("Enter registration number of student ---> ")
            search_reg_no(reg_no)
        elif usr_ch == '2' :
            name = input("Enter name of student ---> ")
            search_name(name)
        elif usr_ch == '3' :
            roll_no = input("Enter Roll Number of student ---> ")
            search_roll_no(roll_no)
        elif usr_ch == '4' :
            mobile_no = input("Enter Mobile Number of student ---> ")
            search_mobile_no(mobile_no)
        elif usr_ch == '5':
            aadhaar = input("Enter Aadhaar Number of student ---> ")
            search_aadhaar(aadhaar)
        elif usr_ch == '6':
            email = input("Enter Email of student ---> ")
            Email(email)
        elif usr_ch == '7':
            break
        

def pay_fees():

    reg_no = input("Enter registration number of student to pay his fees ---> ")
    f_read = open("students.tc", "rb")
    f_post = open("students_temp.tc", "ab")
    Flag = False
    temp_st = students()
    try:
        while True:
            st = pickle.load(f_read)
            if st.Reg_No == reg_no :
                output("Fees paying of: "+st.Name)
                Flag = True
                temp_st = st
                temp_st.PAY_FEES()
                pickle.dump(temp_st, f_post)
            else:
                pickle.dump(st, f_post)
    except EOFError:
        if not Flag :
            output("Record not found")
        f_read.close()
        f_post.close()
        os.remove("students.tc")
        os.rename("students_temp.tc", "students.tc")

def modify_data():
    reg_no = input("Enter registration number of student to modify its record ---> ")
    f_read = open("students.tc", "rb")
    f_post = open("students_temp.tc", "ab")
    Flag = False
    temp_st = students()
    try:
        while True:
            st = pickle.load(f_read)
            if st.Reg_No == reg_no :
                Flag = True
                while True:
                    head("Data Modification Menu")
                    output("Modifying record of : "+st.Name)
                    menu(["1. Modify Registration Number", "2. Modify Roll Number", "3. Modify Name", "4. Modify Father's Name", "5. Modify Mother's Name", "6. Modify Sex", "7. Modify Date of Birth", "8. Modify Age","9. Modify Address" ,"10. Modify Mobile Number" ,"11. Modify E-mail","12. Modify Class","13. Modify Section","14. Modify Stream","15. Modify Fees","16. Modify Mode of Convinience","17. Modify Number of Months of deposited fees", "18. Modify Weight", "19. Modify Height" ,"20. Modify Blood Group" ,"21. Modify Aadhaar" ,"22. Modify all records" ,"23. Exit Data Modification Menu and saving changes"])
                    usr_ch = input("Enter your choice [Modification Menu] ---> ")
                    if usr_ch == '1':
                        temp_st = st
                        temp_st.Reg_No = input("Enter new Registration Number ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '2':
                        temp_st = st
                        temp_st.Roll_No = input("Enter new Roll Number ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '3':
                        temp_st = st
                        temp_st.Name = input("Enter new Name ---> ")    
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '4':
                        temp_st = st
                        temp_st.Father_Name = input("Enter new Father's Name ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '5':
                        temp_st = st
                        temp_st.Mother_Name = raw_input("Enter new Mother's Name ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break  
                    elif usr_ch == '6':
                        temp_st = st
                        temp_st.Sex = raw_input("Enter new SEX [M/F] ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '7':
                        temp_st = st
                        temp_st.DOB = raw_input("Enter new Date of Birth [DDMMYYYY] ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '8':
                        temp_st = st
                        temp_st.Age = input("Enter new Age ---> ")   
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '9':
                        temp_st = st
                        temp_st.Address = raw_input("Enter new Address ---> ") 
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '10':
                        temp_st = st
                        temp_st.Mobile_No = input("Enter new Mobile Number ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '11':
                        temp_st = st
                        temp_st.Email = raw_input("Enter new E-Mail ---> ")   
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '12':
                        temp_st = st
                        temp_st.Class = input("Enter new Class ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '13':
                        temp_st = st
                        temp_st.Section = raw_input("Enter new Section ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '14':
                        temp_st = st
                        temp_st.Stream = raw_input("Enter new stream ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '15':
                        temp_st = st
                        temp_st.Fees = input("Enter new Fees ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '16':
                        temp_st = st
                        temp_st.MOC = raw_input("Enter new Mode of Convinience ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '17':
                        temp_st = st
                        temp_st.Fees_Months = input("Enter update number of months of fees paid ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '18':
                        temp_st = st
                        temp_st.Weight = input("Enter new Weight ---> ")      
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '19':
                        temp_st = st
                        temp_st.Height = input("Enter new Height ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '20':
                        temp_st = st
                        temp_st.B_Group = raw_input("Enter new Blood Group ---> ")
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '21':
                        temp_st = st
                        temp_st.Aadhaar = input("Enter new Aadhaar ---> ")       
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '22':
                        temp_st.GET_DATA(1)
                        pickle.dump(temp_st, f_post)
                        output("Record Modified successfully")
                        break
                    elif usr_ch == '23':
                        break
                    else:
                        output("Please enter valid choice")
                    
            else:
                pickle.dump(st, f_post)
    except EOFError:
        if not Flag :
            output("Record not found")
        f_read.close()
        f_post.close()
        os.remove("students.tc")
        os.rename("students_temp.tc", "students.tc")
    

def remove_data():
    reg_no = input("Enter registration number of student to delete its record ---> ")
    f_read = open("students.tc", "rb")
    f_post = open("students_temp.tc", "ab")
    Flag = False
    try:
        while True:
            st = pickle.load(f_read)
            if st.Reg_No == reg_no :
                Flag = True
                output("Record deleted successfully")
            else :
                pickle.dump(st, f_post)
    except EOFError:
        if not Flag:
            output("Record not found")
        f_read.close()
        f_post.close()
        os.remove("students.tc")
        os.rename("students_temp.tc", "students.tc")


def Main_Menu():
    head("College Management System")
    ch=input("ENTER 1 TO CONTINUE :")
    while True :
        menu(["1. Register a new student", "2. Read all student's record", "3. Search", "4. Pay Fees", "5. Modify Data", "6. Remove Record", "7. Exit"])
        usr_ch = input("Enter your choice [Main Menu] ---> ")
        if usr_ch == '1':
            post_data()
            break
        elif usr_ch == '2':
            show_data()
            break
        elif usr_ch == '3':
            search()
            break
        elif usr_ch == '4':
            pay_fees()
            break
        elif usr_ch == '5':
            modify_data()
            break
        elif usr_ch == '6':
            remove_data()
            break
        elif usr_ch == '7':
            os._exit(1)
        else:
            output("Enter valid Input")
        if ch == 1:
            continue
        
if __name__ == "__main__" :
    Main_Menu()
