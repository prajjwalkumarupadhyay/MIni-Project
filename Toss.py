import random
def Toss():
    toss=[]
    for i in range(100):
        j=random.randint(0,1)
        if (j==0):
            toss.append('H')
        if (j==1):
            toss.append('T')
    print(toss)
                #Under Development
Toss()