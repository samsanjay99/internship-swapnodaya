class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder} | Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest added at {self.interest_rate}%. New balance: ${self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Overdraft used. Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Exceeded overdraft limit!")

print("--- Savings Account Test ---")
savings = SavingsAccount("Alice", 1000, 5.0)
savings.display_balance()
savings.deposit(500)
savings.add_interest()
savings.withdraw(200)

print("\n--- Current Account Test ---")

current = CurrentAccount("Bob", 500, 1000)
current.display_balance()
current.withdraw_with_overdraft(200) 
current.display_balance()