#This Program calculates your total calories and protein intake
import sys,pyinputplus as py
food_calories={'roti':106,
               'milk':149,
               'banana shake':375,
               'dry fruits':145,
               'sattu':41,
               'eggs':78,
               'cooked rice':130,
               'kala channa':3.6}
food_protein={'roti':3.84,
              'milk':7.7,
              'banana shake':14.5,
              'dry fruits':3.65,
              'sattu':2.5,
              'eggs':6.3,
              'cooked rice':2.7,
              'kala channa':0.21}
print('''\n                           Calories and Protein Calculator.\n        
     1. Enter 1 to know your calories and Protein intake
     2. Enter 0 to exit ''')
option=py.inputInt()
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
            Quantity=py.inputFloat('How many Roti you ate:')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='milk':
            calories=food_calories.get('milk')
            protein=food_protein.get('milk')
            Quantity=py.inputFloat('How many glass of milk you drink:')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='banana shake':
            calories=food_calories.get('banana shake')
            protein=food_protein.get('banana shake')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='dry fruits':
            calories=food_calories.get('dry fruits')
            protein=food_protein.get('dry fruits')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='sattu':
            calories=food_calories.get('sattu')
            protein=food_protein.get('sattu')
            Quantity=py.inputFloat('How many Tea spoon:')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='eggs':
            calories=food_calories.get('eggs')
            protein=food_protein.get('eggs')
            Quantity=py.inputFloat('How many eggs you ate:')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='cooked rice':
            calories=food_calories.get('cooked rice')
            protein=food_protein.get('cooked rice')
            Quantity=py.inputFloat('How many grams you ate:')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='kala channa':
            calories=food_calories.get('kala channa')
            protein=food_protein.get('kala channa')
            Quantity=py.inputFloat('How many grams:')
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        else:
            print('This food item is not in the list')
    return Calories_intake,Protein_intake
if option==1:
    print("List of Food items and there calories:",food_calories)
    print()
    print("List of Food items and their Protein:",food_protein)
    Total_Calories_Protein=Protein_Calories()
    print('Your Total Calories and Protien are:',Total_Calories_Protein)
elif option==0:
    sys.exit
 
