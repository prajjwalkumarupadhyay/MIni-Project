import random,sys
print('Carrot in the box by Prajjwal Kumar Upadhyay')
print('--snip--')
player1=input('Human player 1 , enter your name:')
player2=input('Human player 2, enter your name:')
def main():     
      def box():
            print(f'{player1} here is the inside of your box')
            num=random.randint(0,1)
            if num==0:
                  print(f'''
                              ___\/\/___                          
                             |   \/\/   |
                             |   \/\/   |
                             |____||____|        ____________
                            /     ||   /|       /           /|
                           +----------+ |      +-----------+ |
                           |   RED    | |      |   GOLD    | |
                           |   BOX    | |      |   BOX     | |
                           +----------+/       +-----------+/
                              (carrot!)
                               {player1}         {player2}''')
            elif num==1:
                  print(f'''
                              ___\/\/___                          
                             |   \/\/   |
                             |   \/\/   |
                             |____||____|        ____________
                            /     ||   /|       /           /|
                           +----------+ |      +-----------+ |
                           |   GOLD   | |      |    RED    | |
                           |   BOX    | |      |    BOX    | |
                           +----------+/       +-----------+/
                              (carrot!)
                               {player2}        {player1}  ''')
            return (num)
      print('HERE ARE TWO BOXES:')
      print(f''' 
              ___________         ______________
            /           /|       /             /|
            +----------+ |      +-------------+ | 
            |   RED    | |      |   GOLD      | |  
            |   BOX    | /      |    BOX      | /
            +----------+/       +-------------+/
                {player1}             {player2}
      ''')
      print(f'{player1}, you have a RED box in front of you.')
      print(f'{player2}, you have a GOLD box in front of you')
      option=input('Press Enter to continue.')
      if option=='':
            print('--snip--')
      else:
            value=print('Do you want to quite?')
            if value.lower()=='yes':
                  sys.exit('Thank You😄')
            else:
                  print('Playing game from start.')
                  main()
      print(f'When {player2} has closed his/her eyes, press Enter...')
      option=input()
      if option=='':
            num=box()
      option=print('Press Enter to Continue.....')
      if option=='':
            print('--snip--')
      while True:
            print(f'{player1}, Have you seen your box?(Yes/No)')
            value=input()
            if value.lower()=='yes':
                  print('\n'*100)
                  break
            else:
                  box()
                  continue
      print(f'Now {player2}, guess in which box carrot was....')
      ans=input()
      if ans.lower()=='red':
            if num==0:
                  print('Congratulations!!, You guessed it right...')
            else:
                  print('You lost. Better luck next time.')
      elif ans.lower()=='gold':
            if num==1:
                  print('Congratulations!!, You guessed it right...')
            else:
                  print('You lost. Better luck next time.')
      value=input('Do you want to play this game again??(Yes/No)')
      if value.lower()=='yes':
            main()
      else:
            sys.exit('Thank You for playing 😄')
main()
