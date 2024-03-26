

class Restaurant:
    
    name = ''
    category = ''
    rating = 0
    delivery = False

bobs_burgers = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'

bobs_burgers.category = 'Burgers'

bobs_burgers.rating = 4.5

bobs_burgers.delivery = True


# print(bobs_burgers.name) 

print(vars(bobs_burgers)) 