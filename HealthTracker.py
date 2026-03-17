#This Program calculates your total calories and protein intake
import sys 
food_calories={'roti':106,
               'milk':115,
               'banana shake':375,
               'dry fruits':145,
               'sattu':115,
               'eggs':74,
               'cooked rice':130,
               'kala channa':3.6,
               'Dark choclate':54,
               'Alo Paratha':275,
               'Arhar dal':150}
food_protein={'roti':3.84,
              'milk':7,
              'banana shake':14.5,
              'dry fruits':3.65,
              'sattu':6,
              'eggs':6.3,
              'cooked rice':2.7,
              'kala channa':0.20,
              'Dark choclate':1,
              'Alo Paratha':6,
              'Arhar dal':8}
print('''\n\t\tCalories and Protein Calculator.\n        
     1. Enter 1 to know your calories and Protein intake
     2. Enter any key to exit ''')
option=input()
def Protein_Calories():
    print('Enter food items you ate today or type \'exit\' to Exit')
    Calories_intake=0
    Protein_intake=0
    while True:
        food=input('\n')
        if food.lower()=='exit':
            break
        if food.lower()=='roti':
            calories=food_calories.get('roti')
            protein=food_protein.get('roti')
            Quantity=int(input('How many Roti you ate:'))
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='milk':
            calories=food_calories.get('milk')
            protein=food_protein.get('milk')
            Quantity=int(input('How many glass of milk you drunk:'))
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.replace(' ','').lower()=='bananashake':
            calories=food_calories.get('banana shake')
            protein=food_protein.get('banana shake')
            Calories_intake+=(calories)
            Protein_intake+=(protein)
        elif food.replace(' ','').lower()=='dryfruits':
            calories=food_calories.get('dry fruits')
            protein=food_protein.get('dry fruits')
            Quantity=int(input('how much gm'))
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='sattu':
            calories=food_calories.get('sattu')
            protein=food_protein.get('sattu')
            Quantity=int(input('How many times:'))
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.lower()=='eggs':
            calories=food_calories.get('eggs')
            protein=food_protein.get('eggs')
            Quantity=int(input('How many eggs you ate:'))
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.replace(' ','').lower()=='cookedrice':
            calories=food_calories.get('cooked rice')
            protein=food_protein.get('cooked rice')
            Quantity=input('How many gram:')
            Quantity1=int(Quantity[0])
            Calories_intake+=(calories*Quantity1)
            Protein_intake+=(protein*Quantity1)
        elif food.replace(' ','').lower()=='kalachanna':
            calories=food_calories.get('kala channa')
            protein=food_protein.get('kala channa')
            Quantity=int(input('How many grams:'))
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.replace(' ','').lower()=='darkchoclate':
            calories=food_calories.get('Dark choclate')
            protein=food_protein.get('Dark choclate')
            Quantity=int(input('How many cubes:'))
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.replace(' ','').lower()=='aloparatha':
            calories=food_calories.get('Alo Paratha')
            protein=food_protein.get('Alo Paratha')
            Quantity=int(input('How many parathas :'))
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)
        elif food.replace(' ','').lower()=='arhardal':
            calories=food_calories.get('Arhar dal')
            protein=food_protein.get('Arhar dal')
            Quantity=int(input('How many cups :'))
            Calories_intake+=(calories*Quantity)
            Protein_intake+=(protein*Quantity)  
        else:
            print('This food item is not in the list')
    return Calories_intake,Protein_intake
if option=='1':
    print("List of Food items and there calories:",food_calories)
    print()
    print("List of Food items and their Protein:",food_protein)
    Total_Calories_Protein=Protein_Calories()
    print('Your Total Calories and Protien are:',Total_Calories_Protein)
else:
    sys.exit
 