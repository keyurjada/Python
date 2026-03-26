balance = 0

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Withdrawn:", amount)

def check_balance():
    print("Current Balance:", balance)

while True:
    print("\n1.Deposit  2.Withdraw  3.Check Balance  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = float(input("Enter amount: "))
        deposit(amt)

    elif choice == 2:
        amt = float(input("Enter amount: "))
        withdraw(amt)

    elif choice == 3:
        check_balance()

    elif choice == 4:
        break
    else:
        print("Invalid choice")