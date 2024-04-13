
# bestie

# genz_slang = ['bestie', 'tea', 'cap']

# print(genz_slang)

# for i in genz_slang:
#     print(i)

# friend's location 

# friends = (
#     (37.7749, -122.4194), 
#     (40.7128, -74.0060), 
#     (4.624335, -74.063644)
# )

# for i in friends:
#     print(i)

# artifact 

# artifact = {
#    'artist' : 'Leonardo Da Vinci',
#     'title' : 'Mona Lisa',
#     'year' : 1503
# }

# print(artifact)

# print(artifact.keys())

# print(artifact.values())

# print(artifact.items())

# Favorite fruits

# favorite_fruits = {'apple', 'banana', 'orange'}

# friend_favorite_fruits = {'guava', 'grapes', 'kiwi'}

# union_result = favorite_fruits.union(friend_favorite_fruits)

# intersection_result = favorite_fruits.intersection(friend_favorite_fruits)

# difference_result = favorite_fruits.difference(friend_favorite_fruits)

# print(intersection_result)
# print(union_result)
# print(difference_result)

# post game stats  

player_01 = {
    'name' : 'Lebron James',
    'position' : 'Small Forward',
    'jersey_number' : 7,
    'yards' : 25,
    'touchdowns' : 2
}

player_02 = {
    'name' : 'Kevin Durant',
    'position' : 'Power Forward',
    'jersey_number' : 35,
    'yards' : 30,
    'touchdowns' : 3
}

player_03 = {
    'name' : 'Stephen Curry',
    'position' : 'Point Guard',
    'jersey_number' : 30,
    'yards' : 20,
    'touchdowns' : 1
}

player_04 = {
    'name' : 'Kawhi Leonard',
    'position' : 'Shooting Guard',
    'jersey_number' : 2,
    'yards' : 15,
    'touchdowns' : 1
}

players = [player_01, player_02, player_03, player_04]

total_yards = sum([player['yards'] for player in players])
touchdowns = sum([player['touchdowns'] for player in players])

average_yards = total_yards / len(players)
average_touchdowns = touchdowns / len(players)

print('\nAverage yards gained:', average_yards)
print('Average touchdowns:', average_touchdowns)