

# with open('diaries.txt', 'w') as file:
#     file.write('I am a file writer\n')
#     file.write('I am a diary writer')


# with open('diaries.txt', 'r') as file:
#     content = file.read()
#     print(content)

# liked_songs = {
#     'Bad Habits': 'Ed Sheeran',
#     "I'm Just Ken": 'Ryan Gosling',
#     'Mastermind': 'Taylor Swift',
#     'Uptown Funk': 'Mark Ronson ft. Bruno Mars',
#     'Ghost': 'Justin Bieber',
#     'Love Story': 'Taylor Swift'
# }


# def write_liked_songs_to_file(liked_songs, file_name):
#     with open(file_name, 'w') as file:
#         for title, artist in liked_songs.items():
#             file.write(f'{title}  : {artist}\n')


# write_liked_songs_to_file(liked_songs, 'diaries.txt')



# sent_message = 'Hey there! This is a secret message.'
# with open('sent_message.txt', 'w') as file:
#     file.write(sent_message)

# with open('sent_message.txt', 'r+') as file:
    
#     original_message = file.read()
      
#     file.seek(0)
    
#     unsent_message = 'This message has been unsent.'
    
#     file.truncate(len(unsent_message))
    
#     file.write(unsent_message)

# print("Original Message:", original_message)

# print("Unsent Message:", unsent_message)

# import csv

# data_to_write = [
#   ['Name', 'Age', 'Grade'],
#   ['Alice', 25, 'A'],
#   ['Bob', 22, 'B'],
#   ['Charlie', 28, 'A+']
# ]

# with open('output.csv', 'w', newline='') as file:
  
#   csv_writer = csv.writer(file)

#   csv_writer.writerows(data_to_write)


import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('inventory.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except FileNotFoundError:
    print('inventory file not found. Creating a new one...')

    with open('inventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

