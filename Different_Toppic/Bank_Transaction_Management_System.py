class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


# Example usage
account = BankAccount("1234567890", 1000)

print("Welcome to the Bank Transaction Management System!")
print(f"Account Number: {account.account_number}")
print(f"Current Balance: ${account.get_balance()}")

while True:
    print("\nPlease select an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        amount = float(input("Enter the deposit amount: $"))
        account.deposit(amount)
        print(f"Deposit of ${amount} successful!")

    elif choice == "2":
        amount = float(input("Enter the withdrawal amount: $"))
        account.withdraw(amount)
        print(f"Withdrawal of ${amount} successful!")

    elif choice == "3":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")

print("Final Account Details:")
print(f"Account Number: {account.account_number}")
print(f"Current Balance: ${account.get_balance()}")

print("Transaction History:")
for transaction in account.get_transactions():
    print(transaction)
