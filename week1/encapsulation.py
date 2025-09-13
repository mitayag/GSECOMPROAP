class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")
    
    def get_balance(self):
        return self.__balance


# Create an account with an initial balance of 100
account = BankAccount(100)

# Deposit 50
account.deposit(50)
print("Balance after deposit:", account.get_balance())  # 150

# Try to access private attribute directly
try:
    print(account.__balance)  # This will raise an AttributeError
except AttributeError as e:
    print("Error when accessing __balance directly:", e)

# Accessing through name mangling (not recommended, breaks encapsulation)
print("Accessing with name mangling:", account._BankAccount__balance)
