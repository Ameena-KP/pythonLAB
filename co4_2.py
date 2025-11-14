class BankAccount:
    # Method to set account details
    def set_details(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully!")
        print("Updated Balance:", self.balance)

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Withdrawal failed.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully!")
            print("Updated Balance:", self.balance)

    # Method to display account details
    def display(self):
        print("\n----- Account Details -----")
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)


# --- Main Program ---
acc = BankAccount()

print("Enter Account Details:")
acc_no = input("Account Number: ")
name = input("Account Holder Name: ")
acc_type = input("Type of Account (Savings/Current): ")
balance = float(input("Initial Balance: "))

acc.set_details(acc_no, name, acc_type, balance)

acc.display()

amount = float(input("\nEnter amount to deposit: "))
acc.deposit(amount)

amount = float(input("\nEnter amount to withdraw: "))
acc.withdraw(amount)

acc.display()

