math = int(input("Enter Mathematics marks: "))
phy = int(input("Enter Physics marks: "))
chem = int(input("Enter Chemistry marks: "))
total = math + phy + chem
perc = total / 3

if math >= 60 and phy >= 50 and chem >= 40 and perc >= 50:
    print("Eligible for admission")
else:
    print("Not eligible")
