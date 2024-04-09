

# temperature = 12

# fahrerheit = (temperature - 32) / 1.8

# print(fahrerheit)

# bmi

# mass = 61

# height = 1.67

# bmi = mass / height ** 2

# print(bmi)

# hypotenuse

# a = int(input("Enter the value of a: "))

# b = int(input("Enter the value of b: "))

# c = (a ** 2 + b ** 2) ** 0.5

# print(c)

# Currency Converter

# pesos = int(input("What do you have left in pesos? "))

# soles = int(input("What do you have left in soles? "))

# reais = int(input("What do you have left in reais? "))

# total_usd = pesos * 0.051 + soles * 0.26 + reais * 0.18

# print(f"You have {total_usd} dollars left.")

# Heads or Tails

# import random

# num = random.randint(0, 1)  

# if num > 0.5:
#   print('Heads')
# else:
#   print('Tails')

# Grades

# grade = int(input("Enter your grade: "))

# if grade >= 55:
#     print('You have passed')

# else:
#     print('You have failed')

# ph scale

# ph = float(input("Enter the ph value between 7 to 14: "))

# if ph > 7:
#     print('Basic')

# elif ph < 7:
#     print('Acidic')

# else:
#     print('Neutral')

# Magic 8 Ball

# import random

# question = input("Ask the magic 8 ball a question: ")

# num = random.randint(0, 9)

# if num == 0:
#     print('Yes - definitely.')

# elif num == 1:
#     print('It is decidedly so.')

# elif num == 2:
#     print('Without a doubt.')

# elif num == 3:
#     print('Reply hazy, try again.')

# elif num == 4:
#     print('Ask again later.')

# elif num == 5:
#     print('Better not tell you now.')

# elif num == 6:
#     print('My sources say no.')

# elif num == 7:
#     print('Outlook not so good.')

# elif num == 8:
#     print('Very doubtful.')

# else:
#     print('Concentrate and ask again.')


# The Cyclone

# height = int(input("Enter your height: "))

# credits = int(input("Enter the number of credits you have: "))

# if height >= 137 and credits >= 10:
#     print('Enjoy the ride!')

# elif height <= 137 and credits >= 10:
#     print('Sorry, you are too short to ride.')

# elif height >= 137 and credits <= 10:
#     print('Sorry, you do not have enough credits.')

# else:
#     print('You did not meet the requirements.')

# Sorting Hat

# Gryffindor = 0
# Ravenclaw = 0
# Hufflepuff = 0
# Slytherin = 0


# question_1 = input('''Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk
                   
#     : ''')


# if question_1 == '1':

#    Gryffindor += 1
#    Ravenclaw += 1

# elif question_1 == '2':
   
#     Hufflepuff += 1
#     Slytherin += 1

# else:
#     print('Invalid input.')


# question_2 = input('''Q2) When I'm dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold
                   
#     :''')

# if question_2 == '1':

#     Hufflepuff += 2

# elif question_2 == '2':

#     Slytherin += 2

# elif question_2 == '3':

#     Ravenclaw += 2

# elif question_2 == '4':

#     Gryffindor += 2

# else:
#     print('Invalid input.')

# question_3 = input('''Q3) Which kind of instrument most pleases your ear?
                   
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum
                   
#     : ''')

# if question_3 == '1':

#     Gryffindor += 4

# elif question_3 == '2':

#     Hufflepuff += 4

# elif question_3 == '3':

#     Ravenclaw += 4

# elif question_3 == '4':

#     Slytherin += 4

# else:
#     print('Invalid input.')


# houses = {'Gryffindor': Gryffindor, 'Ravenclaw': Ravenclaw, 'Hufflepuff': Hufflepuff, 'Slytherin': Slytherin}

# max_value = max(houses.values())

# max_keys = [k for k, v in houses.items() if v == max_value]

# print(f'You belong to {max_keys[0]}')


# Enter Pin

# print('Welcome to the bank of Python')

# pin = int(input('Enter your pin: '))

# while pin != 1234:

#     pin = int(input('Incorrect Pin. Enter your pin again: '))

# if pin == 1234:
#     print('Pin accepted. You have access to your account.')

 
# guess


# guess = 0

# while guess != 6:

#     guess = int(input('Enter your guess: '))

#     if guess == 6:
#         print('You have guessed correctly.')

#     else:
#         print('Try again.')

# Detention

# for i in range(101):
    
#     print(f'{i}: I will not use Instagram in class')

# 99 Bottles

# for i in range(99, 0, -1):

#     print(f'{i} bottles of beer on the wall, {i} bottles of beer. Take one down, pass it around, {i - 1} bottles of beer on the wall.')
   


# Fizz Buzz

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')

    elif i % 3 == 0:
        print('Fizz')

    elif i % 5 == 0:
        print('Buzz')

    else:
        print(i)