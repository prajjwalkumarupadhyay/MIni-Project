import sys
def choose():
    Days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    month30=[4,6,9,11]
    def Year():
        def century():
            if (x//100==0):
                return 0
            elif (x//100==1):
                return 5
            elif (x//100==2):
                return 3
            elif (x//100==3):
                return 1
        x=(year-1)%400
        Century_odd=century()
        y=x%100
        z=y//4
        odd_days=(((z*2)+(y-z))%7)+ Century_odd
        return odd_days
    def Month():
            monthlist=[3,0,3,2,3,2,3,3,2,3,2,3]
            odd_days=0
            for index, value in enumerate(monthlist):
                odd_days+=value
                if index==(month-2):
                    break
            if (year%4==0): #Checking if the Given year is leap or not 
                odd_days=(odd_days+1)%7
            else:
                odd_days=odd_days%7
            return odd_days
    def Date():
        odd_days=date%7
        return odd_days  
    def correct():
        pass        
    try:
        date=int(input('Date - '))
        if date>31:
            print('Error: There can be at max 31 days in a month.Enter again.')
            choose()
        month=int(input('Month - '))
        if month>12:
            print('Month cannot be more than 12.Enter correct input')
        if month in month30:
            if date>30:
                print('Error:This Month can not have more than 30 days')
                choose()
        if (month==2):
            if date>29:
                print('Error:February cannot have more than 29 days. Enter again')
                choose()
        year=int(input('Year - '))
        if month==2:
            if year%4!=0:
                if date>28:
                    print('This year isnt leap year. So february cannot have more than 28 days.Enter again')
                    choose()
    except ValueError:
        print('Error: Date, Month and Year should be integer.Enter Again.')
        choose()
    odd_year=Year()
    odd_month=Month()
    odd_days=Date()
    #print(odd_year)
    #print(odd_month)
    #print(odd_days)
    total=(odd_days+odd_month+odd_year)%7
    #return str(Days[total])
    print('It was ',str(Days[total]),f" on {date}/{month}/{year}.")
    option=input(('Do you want to start again. Enter YES to continue otherwise space.\n'))
    if option.upper()=="YES":
        choose()
    else:
        sys.exit('Have a nice day!😄')
print('Enter Date, Month and Year in integer.')
choose()
