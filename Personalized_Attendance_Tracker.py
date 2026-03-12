#You can input Your attendance here
def Attendance():
      while True:
        try:
            attended_lectures=int(input('Enter your total attended lectures\n'))
        except ValueError:
            print('Error: Please Enter Valid Input. The entered input Should be integer.')
            continue
        try:
            scheduled_classes=int(input('Total no of classes scheduled\n'))
        except ValueError:
            print('Error: The entered input Should be integer.')
            continue
        return attended_lectures,scheduled_classes
    