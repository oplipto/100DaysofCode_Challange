

hp = 50

score = 0

print('\nWelcome to the Maths RPG game!')

print('You have 100 health points.')

print('You have 0 points.')

print('You will be asked 5 questions.')

print('For each correct answer, you get 20 points.')

print('For each wrong answer, you lose 25 health points.')

print('Good luck!')

ready = input('Are you ready to play? (yes/no): ')

if ready == 'yes':

    print('Question 1: What is 5 * 5?')

    answer1 = int(input('Enter your answer: '))

    if answer1 == 25:
        print('Correct!')
        score += 20

    else:
        print('Wrong!')
        hp -= 25

    print('Question 2: What is 10 * 12?')

    answer2 = int(input('Enter your answer: '))

    if answer2 == 120:
        print('Correct!')
        score += 20

    else:
        print('Wrong!')
        hp -= 25

    

    print('Question 3: What is 5 * 55?')

    answer3 = int(input('Enter your answer: '))
    
    if answer3 == 5 * 55:
        print('Correct!')
        score += 20

    else:
        print('Wrong!')
        hp -= 25

    print('Question 4: What is 20 * 30?')

    answer4 = int(input('Enter your answer: '))

    if answer4 == 20 * 30:
        print('Correct!')
        score += 20

    else:
        print('Wrong!')
        hp -= 25

    print('Question 5: What is 777 - 420?')

    answer5 = int(input('Enter your answer: '))

    if answer5 == 777 - 420:
        print('Correct!')
        score += 20

    else:
        print('Wrong!')
        hp -= 25

    print(f'You have {hp} health points left.')

    print(f'You have {score} points.')

    if hp <= 0:
        print('You have lost all your health points!')
        print('Game Over!')
        print('''Answer of all questions are          
5 * 5 = 25
10 * 12 = 120
5 * 55 = 275
20 * 30 = 600
777 - 420 = 357
''')

    else:
        print('You have completed the game!')
        print('You are a Maths RPG Master!')

else:
    print('Goodbye!')
