import sys
def choose():
    Days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
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
    print('Enter Date, Month and Year in integer.')
    date=int(input('Date - '))
    month=int(input('Month - '))
    year=int(input('Year - '))
    odd_year=Year()
    odd_month=Month()
    odd_days=Date()
    #print(odd_year)
    #print(odd_month)
    #print(odd_days)
    total=(odd_days+odd_month+odd_year)%7
    print('It was ',str(Days[total]),f" on {date}/{month}/{year}.")
    option=input(('Do you want to start again. Enter YES to continue otherwise space.\n'))
    if option.upper()=="YES":
        choose()
    else:
        sys.exit('Have a nice day!😄')
choose()
