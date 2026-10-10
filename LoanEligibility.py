age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit = int(input("Enter credit score: "))

if age >= 21 and income >= 20000 and credit >= 650:
    print("Eligible for loan")
else:
    print("Not eligible")
