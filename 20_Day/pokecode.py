
# Pokecode

# class Pokemon:
#     def __init__(self, entry, names, types, description, is_caught):
#         self.entry = entry
#         self.names = names
#         self.types = types
#         self.description = description
#         self.is_caught = is_caught

#     def speak(self):
#             print(f'{self.names}! {self.names}!')

#     def display_details(self):
#             print(f'Name: {self.names}', f'Type: {self.types}', f'Description: {self.description}', f'Caught: {self.is_caught}', sep='\n')
        

# pikachu = Pokemon(25, 'Pikachu', 'Electric', 'Pikachu is an Electric type Pokémon introduced in Generation 1. It is known as the Mouse Pokémon.', False)

# bulbasaur = Pokemon(1, 'Bulbasaur', 'Grass/Poison', 'Bulbasaur is a Grass/Poison type Pokémon introduced in Generation 1. It is known as the Seed Pokémon.', False)

# charmander = Pokemon(4, 'Charmander', 'Fire', 'Charmander is a Fire type Pokémon introduced in Generation 1. It is known as the Lizard Pokémon.', False)

# squirtle = Pokemon(7, 'Squirtle', 'Water', 'Squirtle is a Water type Pokémon introduced in Generation 1. It is known as the Tiny Turtle Pokémon.', False)

# # print(pikachu.display_details())

# pikachu.speak()

# pikachu.display_details()

# Slot machine 

# import random

# def play_slot_machine():

#     while True:

#         symbols = ['🍒','🍇','🍉','7️⃣']
#         results = random.choices(symbols, k = 3)
#         print(results)

#         if results[0] == results[1] == results[2]:
#             print('You won the Jackpot!💰')
#         else:
#             retry = input('You lost! Would you like to try again? (Y/N): ')
#             if retry.lower() == 'n':
#                 break
#             else:
#                 continue


# play_slot_machine()

# Solar System

from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
    r = 2439.7
elif random_planet == 'Venus':
    r = 6051.8
elif random_planet == 'Earth':
    r = 6371.0
elif random_planet == 'Mars':
    r = 3389.5
elif random_planet == 'Saturn':
    r = 58232.0
else:
    print('Oops! Something went wrong!')

area = 4 * pi * r ** 2

round_area = round(area, 2)

print(f'The area of {random_planet} is {round_area} km²')


