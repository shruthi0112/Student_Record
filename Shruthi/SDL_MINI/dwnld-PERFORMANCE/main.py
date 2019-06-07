from login import try_login, read_login_data
from medical import history, read_medical_data
from attendance import read_attendance_data, disp_attendance
from performance import read_performance_data, analyse_data
from marks import read_marks_data, disp_marks
import matplotlib.pyplot as plt

if __name__ == "__main__":

    logged_in = False
    reg_no = '16BCE2003'

    read_login_data()
    logged_in, reg_no = try_login()
    while(not logged_in):
        print ("Wrong Username or Password")
        logged_in, reg_no = try_login()
    print ("Logged in\n\n")

    print ("Medical history")
    read_medical_data()
    history(reg_no)

    print ("\n\nAttendance")
    read_attendance_data()
    disp_attendance(reg_no)

    print ("\n\nPerformance analysis")
    read_performance_data()
    analyse_data(reg_no)

    print ("\n\nMarks")
    read_marks_data()
    disp_marks(reg_no)

    print ("\n\nLogging out")
