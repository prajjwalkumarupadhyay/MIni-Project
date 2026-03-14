import sys
def ticket():
    try:
        meb=int(input('For how many people do you want movie tickets.\n'))
    except ValueError:
        print('No of members should be Integers.')
        ticket()
    ind={}
    while (len(ind)<meb):
        key=input('Enter member name\n')
        if not key.replace(" ","").isalpha():
            print('The name should be a String.')
            continue
        try:
            value=int(input('Enter member age\n'))
        except ValueError:
            print('Error: age should be in integer. Enter name and age again.')
            continue
        ind[key]=value
    #print(ind)
    def Price():
        print('For which day do you want the tickets.')
        import Calender
        day=Calender.choose()
        price=0
        for i in ind.values():
            if i <18:
                price+=8
            elif i >=18:
                price+=20
        if day=='Wednesday':
            price=price-(meb*2)
        return price
    print('You have to pay:',Price(),'Rs')
print('Do you want to buy ticket for movie. Enter Yes to continue otherwise click any key.')
response=input()
if response.capitalize()=='Yes':
    ticket()
else:
    sys.exit('Thank you!')
