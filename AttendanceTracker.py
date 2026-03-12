from  Personalized_Attendance_Tracker import Attendance # To Enter or Re Enter your attendance
def Global():
    def Days():
        day=[]
        while True:
            value=input()
            if value.lower()=='d':
                break
            elif value.lower()=='sunday':
                print('Sunday is a holiday.')
                continue
            elif value.capitalize() not in lec:
                print('Please enter valid input.')
                continue
            day.append(value.capitalize())
        return day
    lec={'Monday':5,
          'Tuesday':7,
          'Wednesday':5,
          'Thursday':6,
          'Friday':5,
          'Saturday':5}
    print("Enter on which day you were present and  Type (d)one when you have entered the value.")
    present=Days()
    print(present)
print('''Track Your Attendance:
      Do You want to Re-enter Your Attendace''')
attendance=input()
if attendance.lower()=='yes':
    print(Attendance())
Global()
    