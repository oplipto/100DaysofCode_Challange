

class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):

        print(self.name + '' + self.name)

    
    def display_details(self):

        print("Entry number: ", self.entry)
        print("Name: ", self.name)
        print("Types: ", self.types)
        print("Description: ", self.description)

    
pikachu = Pokemon(25, 'Pikachu', 'Electric', 'Mouse Pokemon', False)

# pikachu.speak()

pikachu.display_details()
