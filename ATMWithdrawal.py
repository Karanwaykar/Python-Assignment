pin = int(input("Enter PIN: "))
balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if pin == 1234:  # Example PIN
    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawal successful. Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid PIN")
