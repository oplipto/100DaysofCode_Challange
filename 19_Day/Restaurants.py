
# # Restaurant

# class Restaurant:
#     name = 'Bob\'s Burgers'
#     category = 'American Diner'
#     rating = 4.7
#     delivery = False

# Taj = Restaurant()

# continentals = Restaurant()

# Taj.name = 'Taj Hotel'
# Taj.category = 'Indian'
# Taj.rating = 4.9
# Taj.delivery = True

# continentals.name = 'Continentals'
# continentals.category = 'Continental'
# continentals.rating = 4.8
# continentals.delivery = True

# print(vars(continentals))
# # print(vars(Taj))

# Favorite Cities

# class city:
#     def __init__(self, name, country, population, landmark):
#         self.name = name
#         self.country = country
#         self.population = population
#         self.landmark = landmark


# japan = city('Tokyo', 'Japan', 13929286, 'Tokyo Tower')

# usa = city('New York', 'USA', 8336817, 'Statue of Liberty')

# print(vars(japan))

# print(vars(usa))

# Bank Account

class BankAccount:
    def __init__ (self, firstname, lastname, account_id, account_type, pin, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient Funds'
        else:
            self.balance -= amount
            return self.balance
        
    def get_balance(self):
        return self.balance
        

account = BankAccount('John', 'Doe', 123456789, 'Savings', 1234, 45.77)

# print(vars(account))

print(account.deposit(96))

print(account.withdraw(25))

print(account.get_balance())
