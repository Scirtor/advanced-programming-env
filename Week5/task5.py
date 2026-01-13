class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance


    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive")
            return
        if amount > self.__balance:
            print("Insufficient balance")
            return
        self.__balance -= amount
    def get_balance(self):
        return self.__balance



def run():
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    acc.withdraw(30)
    acc.withdraw(500)

    print(f"Current balance: {acc.get_balance()}")