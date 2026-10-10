income = float(input("Enter annual income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = 0.05 * (income - 250000)
elif income <= 1000000:
    tax = 12500 + 0.2 * (income - 500000)
else:
    tax = 112500 + 0.3 * (income - 1000000)
print("Tax payable:", tax)
