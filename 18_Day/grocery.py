
# grocery

# grocery = ['🥚 Eggs', '🥑 Avocados', '🍪 Cookies', '🌶 Hot Pepper Jam', '🫐 Blueberries', '🥦 Broccoli']

# print(grocery)

# todo

# todo = ['🏦 Get quarters.', '🧺 Do laundry.', '🌳 Take a walk.', '💈 Get a haircut.', '🍵 Make some tea.', '💻 Complete Lists chapter.', '💖 Call mom.', '📺 Watch My Hero Academia.'
# ]

# print(todo[0: 2])

# print(todo[2: 5])

# print(todo[9])

# inventory

# lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

# print(min(lego_parts))

# print(max(lego_parts))

# book club 

# books = ['📚 The Great Gatsby', '📗 The Bell Jar', '📕 The Catcher in the Rye', '📙 The Color Purple', '📘 The Joy Luck Club', '📔 The House on Mango Street', '📒 The Bluest Eye', '📖 The Sun Also Rises', '📓 The Glass Castle', '📙 The Color of Water', '📚 The Great Gatsby', '📚 The Great Gatsby']

# books.append('📚 Zero to Sold')

# books.remove('📗 The Bell Jar')

# books.pop(6)

# books.clear()

# books.copy()

# books.count('📚 The Great Gatsby')

# books.reverse()

# books.sort()

# print(books)

# Mixtape

# playlist = ['🎵 "Lose Yourself" by Eminem', '🎶 "Dancing Queen" by ABBA', '🎵 "Smooth" by Santana', '🎶 "Unchained Melody" by The Righteous Brothers', '🎵 "Hey Jude" by The Beatles', '🎶 "Billie Jean" by Michael Jackson', '🎵 "Rolling in the Deep" by Adele', '🎶 "Bohemian Rhapsody" by Queen', '🎵 "Hotel California" by The Eagles', '🎶 "I Will Always Love You" by Whitney Houston', '🎵 "Thriller" by Michael Jackson', '🎶 "Like a Rolling Stone" by Bob Dylan']

# # for song in range(len(playlist)):

# #     print(playlist[song])
    

# for i in playlist:

#     print(i)

# bucket list

# things_to_do = [
#   '🚀 Create the dopest learn to code platform ever.',
#   '⛰️ Hike the Pacific Crest Trail.',
#   '🏡 Build an A-frame house and raise some goats.',
#   '🌏 Live somewhere in Asia for a year.',
#   '🎸 Release an album.',
#   '📝 Write a book.',
#   '🏆 Reach 100k subscribers on YouTube.',
#   '🚐 Road trip with the fam.',
#   '🍳 Open a cozy diner upstate.',
#   '👴🏻 Grow old with no regrets.'
# ]

# for i in range(len(things_to_do)):

#     print(f'{i + 1} : {things_to_do[i]}')

# Fortune cookie

# import random

# def fortune():
    
#    fortunes = [
      
#         "Don't pursue happiness - create it.",
#         "All things are difficult before they are easy.",
#         "The early bird gets the worm, but the second mouse gets the cheese.",
#         "Someone in your life needs a letter from you.",
#         "Don't just think. Act!",
#         "Your heart will skip a beat.",
#         "The fortune you search for is in another cookie.",
#         "Help! I'm being held prisoner in a Chinese bakery."
         
#           ]
   
#    print(random.choice(fortunes))

# fortune()

# Mars Orbiter

# def distance_to_miles(kilometers):

#     miles = kilometers / 1.60934

#     return miles

# result = distance_to_miles(100)

# print(result)

# calculator

# def add(a, b):

#     return a + b

# def subtract(a, b):

#     return a + b

# def multiply(a, b):

#     return a * b

# def divide(a, b):

#     return a / b

# def exp(a, b):

#     return a ** b

# print(add(5,6))

# print(subtract(10, 6))

# print(multiply(10, 87))

# print(divide(12, 4))

# print(exp(10, 7))

# Stocks 

# stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

# def price_at(x):

#     return stock_prices[x - 1]

# def max_price(a, b):

#     return max(stock_prices[a - 1:b])


# def min_price(a, b):

#     return min(stock_prices [a -1:b])


# print(price_at(4))

# print(int(max_price(2, 8)))

# print(int(min_price(4, 13)))

# Food Ordering System
 
def welcome():

    print("Welcome to the Food Ordering System!")
    print("Here are the items available for order:")
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")





def get_item(item_number):

    menu = {1: '🍔 Cheeseburger',
        2: '🍟 Fries',
        3: '🥤 Soda',
        4: '🍦 Ice Cream',
        5: '🍪 Cookie'
}
    
    return menu.get(item_number)


def main():

    welcome()

    while True:

        try:

            item_number = int(input('Enter the number of food you want to order (1-5) : '))
            if 1 <= item_number <= 5:
                item_name = get_item(item_number)
                print('You Ordered', item_name)
                break
            else:
                print('Please enter a number between 1 to 5! ')

        except ValueError:
            print('Please enter a valid number! ')


if __name__ == '__main__':
   main()
            

