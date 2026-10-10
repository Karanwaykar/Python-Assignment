basic = float(input("Enter basic salary: "))
DA = 0.1 * basic
HRA = 0.2 * basic
gross = basic + DA + HRA
tax = 0.05 * gross
net = gross - tax
print("Gross:", gross, "Tax:", tax, "Net:", net)
