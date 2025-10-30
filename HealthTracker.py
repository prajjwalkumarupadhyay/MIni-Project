#This Program calculates your total calories and protein intake
import sys,pyinputplus as py
food_calories={'roti':106,'milk':149,'banana shake':375,'dry fruits':145,'sattu':41,'eggs':78,'cooked rice':130,'kala channa':3.6}
food_protein={'roti':3.84,'milk':7.7,'banana shake':14.5,'dry fruits':3.65,'sattu':2.5,'eggs':6.3,'cooked rice':2.7,'kala channa':0.21}
print('''             Calories and Protein Calculator.        
     1. Enter 1 to know your calories and Protein intake
     2. Enter 0 to exit ''')
option=py.inputInt('')
def Protein_Calories():
    print('Enter food items you ate today or type \'exit\' to Exit')
    Calories_intake=0
    Protein_intake=0
    while True:
        food=input()
        if food.lower()=='exit':
            break
        if food.lower()=='roti':
            calories=food_calories.get('roti')
            protein=food_protein.get('roti')
            Quantity=py.inputFloat('How many Roti\'s you ate\n')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='milk':
            calories=food_calories.get('milk')
            protein=food_protein.get('milk')
            Quantity=py.inputFloat('How many glass of milk you drink\n')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
    return Calories_intake and Protein_intake
if option==1:
    print("List of Food items and there calories:",food_calories)
    print()
    print("List of Food items and their Protein:",food_protein)
    Total_Calories_Protein=Protein_Calories()
    print('Your Total Calories and Protien are:',Total_Calories_Protein)
elif option==0:
    sys.exit
