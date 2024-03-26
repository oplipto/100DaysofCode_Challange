
class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = ''
        self.last_name = ''
        self.account_id = int()
        self.account_type = ''
        self.pin = int()
        self.balance = float()

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        
        else:
            self.balance -= amount
            return self.balance
        
    def display_balance(self):
        return self.balance
    

account1 = BankAccount('John', 'Doe', 123456, 'Checking', 1234, 1000)

# account1.deposit(96)

print(account1.deposit(96))

# account1.withdraw(25)

print(account1.withdraw(25))

print("Current account balance: ", account1.display_balance())