# Quiz Program
import random

questionBank = {'Mammal':'Which type of animal has warm blood?',
                'Egg':'What does the chicken lay?',
                'Rupees':'What is the currency if Nepal?'}

"""
questions = list(questionBank.values())
rnd = random.randint(0,len(questionBank)-1)
print(questions[rnd])
"""

def quiz(bank):
    score = 0
    for key,value in bank.items():
        answer = input(value +': ')
        if answer.strip().upper() == key.strip().upper():
            print('Correct')
            score += 1
        else:
            print('Your answer is wrong')
    return score

score = quiz(questionBank)

if score == 3:
    print('\nWell Done! Your Score is ',score,'/3')
elif score == 2:
    print('\nYour Score is ',score,'/3')
else:
    print('\nPlease study hard and take retest next time. Your score is ',score,'/3')

