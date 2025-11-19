import sys,random
print('Bagels, a deductive logic game.')
print('''i am thinking of a 3-digit number . Try to guess what it is.
      
      Here are some clue:
      When i say :      That means:
        Pico             One digit is correct but in the wrong position
       Fermi             One position is correct but in the right position
      Bagels             No digit is correct ''')
SecretNumber=random.randint(100,999)
Secretdigit=[]
for d in str(SecretNumber):
    Secretdigit.append(int(d))
print('I have thought up a number.')
print('You have 10 guesses to get it.')
def play_game():
    print("Guess the number or type 'exit' to end the Game.")
    for i in range(1,11):
        GuessedNumber=input()
        GuessedDigit=[int(d) for d in str(GuessedNumber)]
        if GuessedNumber.lower()=='exit':
            sys.exit()
        elif GuessedDigit==Secretdigit:
            print(f'Fermi,Fermi,Fermi!,You have guessed the number in {i} guesses.')
        if GuessedDigit[0] in Secretdigit:
            if GuessedDigit[0]==Secretdigit[0]:
                print('fermi')
            else:
                print('Pico')
        if GuessedDigit[1] in Secretdigit:
            if GuessedDigit[1]==Secretdigit[1]:
                print('fermi')
            else:
                print('Pico')
        if GuessedDigit[2] in Secretdigit:
            if GuessedDigit[2]==Secretdigit[2]:
                print('fermi')
            else:
                print('Pico')
        all_condition=True
        for d in GuessedDigit:
            if d in Secretdigit:
                all_condition=False
                break
            if all_condition:
                print('Bagel')
        if i>=10:
            print('chances over:')
            break
    print('The number I was thinking:',SecretNumber)
while True:
    play_game()
    again=input('Do you want to continue playing this game.')
    if again.lower()=='yes':
        continue
    else:
        break

