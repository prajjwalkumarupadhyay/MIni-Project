#! python3
# randomQuiz.py - Creates quizzes with questions and answers
# in random order , along with the answer key 

import random , os
os.mkdir('/Users/knight/Random_Quiz')
os.chdir('/Users/knight/Random_Quiz')
countries_capitals = {
    "Japan": "Tokyo",
    "Canada": "Ottawa",
    "Brazil": "Brasília",
    "Australia": "Canberra",
    "Egypt": "Cairo",
    "Germany": "Berlin",
    "South Africa": "Pretoria",
    "Argentina": "Buenos Aires",
    "Russia": "Moscow",
    "Mexico": "Mexico City",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Turkey": "Ankara",
    "Kenya": "Nairobi",
    "Nigeria": "Abuja",
    "Indonesia": "Jakarta",
    "South Korea": "Seoul",
    "Thailand": "Bangkok",
    "Vietnam": "Hanoi",
    "Philippines": "Manila",
    "Saudi Arabia": "Riyadh",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Israel": "Jerusalem",
    "Greece": "Athens",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Switzerland": "Bern",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Poland": "Warsaw",
    "Ukraine": "Kyiv",
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Ireland": "Dublin",
    "New Zealand": "Wellington",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Peru": "Lima",
    "Venezuela": "Caracas",
    "Cuba": "Havana",
    "Morocco": "Rabat",
    "Ethiopia": "Addis Ababa",
    "Ghana": "Accra",
    "Malaysia": "Kuala Lumpur",
    "Singapore": "Singapore",
    "India": "New Delhi",
    "Bangladesh": "Dhaka",
    "Sri Lanka": "Sri Jayawardenepura Kotte"
}
print('---snip---')
print('How many Questions you want in your Quiz.')
while True:
    try:
        value=int(input())
    except ValueError:
        print('Entered value should be an Integer.')
        continue
    break
for quizNum in range(value):
    quizFile=open(f'capitalsquiz{quizNum+1}.txt','w')
    answerKeyFile=open(f'capitalsquiz_answers{quizNum+1}.txt','w')

    # Write out the header for the quiz
    quizFile.write('Name:\n\n Dates:\n\n Period:\n\n')
    quizFile.write((' '*20)+f'Country  Capitals Quiz (form{quizNum+1})')
    quizFile.write('\n\n')

    countries=list(countries_capitals.keys())
    random.shuffle(countries) # Shuffle the order of the states

    for questionNum in range(50):
        correctAnswer=countries_capitals[countries[questionNum]]
        wrongAnswer=list(countries_capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer=random.sample(wrongAnswer,3)
        answerOptions=wrongAnswer+[correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write(f'{questionNum+1}. What is the Capital of {countries[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"{'ABCD'[i]}.{answerOptions[i]}\n")
        quizFile.write('\n')
        answerKeyFile.write(f"{questionNum+1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
    quizFile.close()
    answerKeyFile.close()
