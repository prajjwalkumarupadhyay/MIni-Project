def choose():
    def Year():
        def century():
            if (x//100==1):
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
        if (year%4==0): #Checking if the Given year is leap or not 
            monthlist1=[3,1,3,2,3,2,3,3,2,3,2,3]
            odd_days=0
            for x in monthlist1:
                odd_days+=x
                for i in range():
                    pass # Under Development
    print('Enter Date, Month and Year in integer.')
    date=int(input('Date - '))
    month=int(input('Month - '))
    year=int(input('Year - '))
    odd_year=Year()
    odd_month=Month()
    print(odd_year)
choose()