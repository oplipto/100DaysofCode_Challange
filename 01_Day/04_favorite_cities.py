
class city:
    def __init__(self, name, country, population, landmarks, nickname, founding_year, mayor):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.nickname = nickname
        self.founding_year = founding_year
        self.mayor = mayor



hometown = city('New York', 'USA', 8_336_817, ['Statue of Liberty', 'Empire State Building', 'Central Park'], 'The Big Apple', 1624, 'Bill de Blasio')

visit = city('Paris', 'France', 2_148_271, ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'], 'The City of Light', 259, 'Anne Hidalgo')

print("hometown: ", vars(hometown))

print('*' * 144)

print("visit: ", vars(visit))

