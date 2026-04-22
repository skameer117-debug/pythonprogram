class BankAccount:
    def __init__(self, name, balance):
        self.name = name          # instance variable
        self.balance = balance   # initialized using constructor

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


# ---- Main Program ----
name = input("Enter your name: ")
balance = float(input("Enter initial balance: "))

# Constructor is called here
account = BankAccount(name, balance)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)

    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)

    elif choice == 3:
        account.show_balance()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")